"""
"""
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Customer(AbstractBaseUser, PermissionsMixin):
    """
    Main User table for SureBuddy server
    """
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    # email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)
    dob = models.DateField()

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dob']

    objects = CustomUserManager()

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'customer'
        verbose_name = _('customer')
        verbose_name_plural = _('Customers')
        ordering = ['id',] # Set it as required.

    def __str__(self):
        return '{id} <{name}>'.format(
            id=self.id,
            name=self.first_name,
        )

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def is_super_user(self):
        return self.is_superuser
