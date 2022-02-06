"""
"""
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
# from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

from policy.models import Quote, Policy, UserPolicyHistory

Customer = get_user_model()


class QuoteCreateSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Quote
        fields = ('id', 'quote_type', 'customer', 'sum_insured')

    def validate_sum_insured(self, value):
        """
        """
        if not value > 0 :
            message = _('Sum insured should be greater then 0.')
            raise serializers.ValidationError(message)
        return value

    def validate(self, attrs):
        # common validations
        return attrs


class QuoteListSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Quote
        fields = ('id', 'quote_type', 'customer', 'sum_insured', 'status')


class PolicyListSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Policy
        fields = ('id', 'customer', 'quote', 'is_active')


class PolicyHistoryListSerializer(serializers.ModelSerializer):
    """
    """
    policy = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()

    class Meta:
        model = UserPolicyHistory
        fields = (
            'id', 'quote', 'quote', 'status', 'created_at', 'updated_at',
            'policy', 'customer'
        )

    def get_policy(self, obj):
        return obj.quote.policy_set.all().first().id # query can be optimized

    def get_customer(self, obj):
        return obj.quote.policy_set.all().first().customer.id # query can be optimized
