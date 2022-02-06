"""
"""
from django.urls import path

from rest_framework.routers import SimpleRouter

from policy import views

router = SimpleRouter()
router.register(r'quote', views.QuoteViewSet, "quote")
router.register(r'policy', views.PolicyViewSet, "policy")

urlpatterns = [
]

urlpatterns += router.urls
