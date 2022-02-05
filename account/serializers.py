"""
"""
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation as validators

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse

Customer = get_user_model()


class CustomerRegisterSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'dob', 'password',)
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def validate_password(self, value):
        validators.validate_password(password=value)
        return value

    def create(self, validated_data):
        """
        """
        password = validated_data.get('password')
        user = super(CustomerRegisterSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomerGetSerializer(serializers.ModelSerializer):
    """
    NOTE: Customer should be authenticated or there should be user in request.user
        As request.user is used in serialzier to fetch the user related data.
    """
    # profile_picture = serializers.SerializerMethodField()

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'dob')
