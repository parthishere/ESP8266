from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth.models import User
import datetime

from rest_framework.decorators import api_view


from index.models import Esp8266
from .serializers import EspSerializer


@api_view(['GET'])
def get_request_view(request):
    print(request.params)