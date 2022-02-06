"""
"""
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy

from rest_framework import status, generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from account.serializers import CustomerRegisterSerializer
from account.serializers import CustomerGetSerializer

Customer = get_user_model()


def get_login_response(request, user):
    """
    """
    user = Customer.objects.get(id=user.id)
    token, created = Token.objects.get_or_create(user=user)
    serialzier = CustomerGetSerializer(user, context={'request': request})
    response = serialzier.data
    response.update({'token': token.key})
    return response


class RegisterCustomerView(generics.CreateAPIView):
    """
    ** POST DATA **

        {
            "first_name": "guido",
            "last_name": "rossum",
            "dob": "2021-12-12",
            "password": "StR0Ng@Pass"
        }
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        response = get_login_response(request, user)
        return Response(response, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        instance = serializer.save()
        return instance
