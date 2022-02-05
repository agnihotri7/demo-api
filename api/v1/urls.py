"""
"""
from django.urls import path, include

from api.v1 import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
]
