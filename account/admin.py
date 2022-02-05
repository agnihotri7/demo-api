"""
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import UserCreationForm, UserChangeForm

Customer = get_user_model()


class CustomerAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Customer
    list_display = ('id', 'first_name', 'last_name', 'dob', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': (
            'dob', 'password',
            )
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('dob',
            'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('first_name',)
    ordering = ('first_name',)


admin.site.register(Customer, CustomerAdmin)
