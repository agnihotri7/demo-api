"""
"""
from rest_framework import serializers
from rest_framework import status, generics, viewsets
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.decorators import api_view, permission_classes, parser_classes, action

from policy.models import Quote, Policy, UserPolicyHistory
from policy.serializers import QuoteCreateSerializer
from policy.serializers import QuoteListSerializer
from policy.serializers import PolicyListSerializer
from policy.serializers import PolicyHistoryListSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteCreateSerializer
    # permission_classes = [IsAuthenticated,] # permission may need to be changed based on who is going to create the quote

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuoteListSerializer
        return QuoteCreateSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quote = self.perform_create(serializer)
        response = {
            'id': quote.id,
            'quote_type': quote.quote_type,
            'customer': quote.customer.id,
            'sum_insured': quote.sum_insured
        }
        return Response(response, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.status = Quote.QUOTED
        instance.save() # this extra db hit can be saved
        # save policy history
        UserPolicyHistory.objects.create(
            quote=instance,
            status=instance.status
        )
        return instance

    def update(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(methods=['PUT',], detail=True)
    def accept(self, request, pk=None):
        # add validations
        instance = self.get_object()
        instance.status = Quote.ACCEPTED
        instance.save()

        # save policy history
        UserPolicyHistory.objects.create(
            quote=instance,
            status=instance.status
        )

        response = {
            "message": "Quote accepted successfully"
        }
        return Response(response)

    @action(methods=['PUT',], detail=True)
    def payment(self, request, pk=None):
        # add validations only accepted quote payment can be done
        # call payment process and save payment info in a table

        instance = self.get_object()
        instance.status = Quote.PAID # there can be a separate functionality to mark the policy active later on
        instance.save()

        # save policy history
        UserPolicyHistory.objects.create(
            quote=instance,
            status=Quote.PAID
        )

        # create Policy
        Policy.objects.create(
            quote=instance,
            customer=instance.customer,
            is_active=True
        )

        # update quote status to activated after policy created
        instance.status = Quote.ACTIVATED
        instance.save()

        # save policy history
        UserPolicyHistory.objects.create(
            quote=instance,
            status=Quote.ACTIVATED
        )

        response = {
            "message": "Quote payment done"
        }
        return Response(response)


class PolicyViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Policy.objects.all()
    serializer_class = PolicyListSerializer
    # permission_classes = [IsAuthenticated,] # only requesting user policy will be returned

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PolicyListSerializer
        return PolicyListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.status = Quote.QUOTED
        instance.save() # this extra db hit can be saved
        # save policy history
        UserPolicyHistory.objects.create(
            quote=instance,
            status=instance.status
        )
        return instance

    def update(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @action(methods=['GET',], detail=True, serializer_class=PolicyHistoryListSerializer)
    def history(self, request, pk=None):
        # add validations
        instance = self.get_object()
        instance.status = Quote.ACCEPTED
        instance.save()

        # list policy history
        queryset = UserPolicyHistory.objects.filter(
            quote__customer_id=1,
            # quote__policy_id=1
        )

        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = PolicyHistoryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
