"""
"""
from django.contrib import admin
from django.contrib.auth import get_user_model

from policy.models import Quote, Policy, UserPolicyHistory

Customer = get_user_model()


class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    list_display = ('id', 'quote_type', 'status', 'customer')
    list_filter = ()
    search_fields = ('id', 'quote_type', 'status', 'customer')
    ordering = ('id', 'quote_type', 'status', 'customer')

admin.site.register(Quote, QuoteAdmin)


class PolicyAdmin(admin.ModelAdmin):
    model = Policy
    list_display = ('id', 'quote_id', 'is_active', 'customer')
    list_filter = ()
    search_fields = ('id', 'quote_id', 'is_active', 'customer')
    ordering = ('id', 'quote_id', 'is_active', 'customer')

admin.site.register(Policy, PolicyAdmin)


class UserPolicyHistoryAdmin(admin.ModelAdmin):
    model = UserPolicyHistory
    list_display = ('id', 'status', 'quote_id')
    list_filter = ()
    search_fields = ('id', 'status', 'quote')
    ordering = ('id', 'status', 'quote')

admin.site.register(UserPolicyHistory, UserPolicyHistoryAdmin)
