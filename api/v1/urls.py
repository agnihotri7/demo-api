"""
"""
from django.urls import path, include

from api.v1 import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    # path('account/', include('account.urls')), # ideally all account related urls should follow account/ prefix in url
    path('', include('account.urls')),
    path('', include('policy.urls')),
]
