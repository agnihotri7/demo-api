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
        ])),
    ]))
