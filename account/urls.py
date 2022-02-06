"""
"""
from django.urls import path
from account import views

urlpatterns = [
    path('create_customer/', views.RegisterCustomerView.as_view(), name='create-customer'),
]
