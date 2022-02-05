"""
"""
from collections import OrderedDict

from django.conf import settings

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


@api_view(['GET'])
def api_root(request, user_type=None):
    if not settings.ENABLE_API_ROOT:
        return Response(dict())

    if user_type is None:
        return Response(OrderedDict([
            # your apis url links here
        ]))
