"""
"""
from collections import OrderedDict

from django.conf import settings
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    Each API Endpoint contains corresponding documentation.
    """
    if not settings.ENABLE_API_ROOT:
        return Response(dict())

    return Response(OrderedDict([
        ('Registration', OrderedDict([
            ('Create Customer', reverse('v1:create-customer', request=request, format=format, kwargs={})),

            ('Quote create/list', reverse('v1:quote-list', request=request, format=format, kwargs={})),
            ('Quote detail', reverse('v1:quote-detail', request=request, format=format, kwargs={'pk': 1})),
            ('Quote accept', reverse('v1:quote-accept', request=request, format=format, kwargs={'pk': 1})),
            ('Quote payment', reverse('v1:quote-payment', request=request, format=format, kwargs={'pk': 1})),

            ('Policy list', reverse('v1:policy-list', request=request, format=format, kwargs={})),
            ('Policy detail', reverse('v1:policy-detail', request=request, format=format, kwargs={'pk': 1})),
            ('Policy history', reverse('v1:policy-history', request=request, format=format, kwargs={'pk': 1})),
        ])),
    ]))
