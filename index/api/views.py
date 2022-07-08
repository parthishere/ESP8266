from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.contrib.auth.models import User
import datetime
from ..forms import SaveForm

from rest_framework.decorators import api_view


from index.models import Applience, Esp8266
from .serializers import AppliencesSerializer, EspSerializer


@api_view(['GET'])
def return_data_to_esp_view(request):
    message = {}
    username = request.params.get('username')
    unique_id = request.params.get('uqid')
    
    
    try:
        esp = Esp8266.objects.get(user__username=username, unique_id=unique_id)
        
        appliences = Applience.objects.filter(esp=esp).order_by("-id")
    except:
        message = {"error": "404", "data": "Object not found !"}
        return Response(message)
    
    serializer = AppliencesSerializer(appliences, many=True)
    return Response(serializer.data)

from django.views.decorators.csrf import csrf_exempt


@api_view(['POST', 'PUT', 'PATCH'])
@csrf_exempt
def get_posted_data_from_esp(request):
    message = {}
    
    form = SaveForm(request.POST)
    form.is_valid()
    
    unique_id = request.params.get('unique_id')
    username = request.params.get('username')
    
    password = form.validated_data.get('password')
    D0 = form.validated_data.get('D0')
    D1 = form.validated_data.get('D1')
    D2 = form.validated_data.get('D2')
    D3 = form.validated_data.get('D3')
    D4 = form.validated_data.get('D4')
    D5 = form.validated_data.get('D5')
    A0 = form.validated_data.get('A0')
    
    try:
        esp = Esp8266.objects.get(user__username=username, unique_id=unique_id)
        
        appliences = Applience.objects.filter(esp=esp).order_by("-id")
    except:
        message = {"error": "404", "data": "Object not found !"}
        return Response(message)
    
    print(appliences)
    
    return Response("Got the data")
    
        
    
    
    
    