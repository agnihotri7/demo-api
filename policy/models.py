"""
"""
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

Customer = get_user_model()


class Quote(models.Model):
    """
    Policy details table
    """
    QUOTED, ACCEPTED, PAID, ACTIVATED, CANCELLED, EXPIRED = "quoted", "accepted", "paid", "activated", "cancelled", "expired"
    STATUS = (
        (QUOTED, 'Quoted'),
        (ACCEPTED, 'Accepted'),
        (PAID, 'Payment'),
        (ACTIVATED, 'Activated'),
        (CANCELLED, 'Cancelled'),
        (EXPIRED, 'Expired'),
    )
    quote_type = models.CharField(_('Type'), max_length=200)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=30)
    sum_insured = models.FloatField(_('Sum insured'))
    # include more fields like duration for which the policy is valid

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'quote'
        verbose_name = _('Quote')
        verbose_name_plural = _('Quotes')

    def __str__(self):
        return "{}-{}".format(self.id, self.user.id)


class Policy(models.Model):
    """
    User Policy details table
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.RESTRICT) # should be one to one relation
    is_active = models.BooleanField(_('active'), default=True) # mark inactive if quote entry status changes to cancelled/expired
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'policy'
        verbose_name = _('Policy')
        verbose_name_plural = _('Policies')

    def __str__(self):
        return "{}-{}".format(self.id, self.user.id)


class UserPolicyHistory(models.Model):
    """
    UserPolicyHistory
    """
    quote = models.ForeignKey(
        Quote, on_delete=models.RESTRICT
    )
    status = models.CharField(choices=Quote.STATUS, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True) # credit time
    updated_at = models.DateTimeField(auto_now=True)   # debit/expired time

    class Meta:
        db_table = 'policy_history'
        verbose_name = _('Policy History')
        verbose_name_plural = _('Policies Histories')

    def __str__(self):
        return "{}".format(self.id)
