"""
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

Customer = get_user_model()


class CustomerCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Customer
        fields = ('first_name', 'last_name', 'dob')


class CustomerChangeForm(UserChangeForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'dob')
