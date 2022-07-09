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
    username = request.query_params.get('username')
    unique_id = request.query_params.get('uqid')
    
    print(username)
    print(unique_id)
    
    
    try:
        esp = Esp8266.objects.get(user__user__username=username, unique_id=unique_id)
        
        appliences = Applience.objects.filter(esp=esp).order_by("-id")
    except:
        message = {"error": "404", "data": "Object not found !"}
        return Response(message)
    
    serializer = AppliencesSerializer(appliences, many=True)
    print(serializer.data)
    return Response(serializer.data)

from django.views.decorators.csrf import csrf_exempt


@api_view(['POST', 'PUT', 'PATCH'])
@csrf_exempt
def get_posted_data_from_esp(request):
    message = {}
    appliences = None
    form = SaveForm(request.POST)
    form.is_valid()
    
    unique_id = request.query_params.get('uqid').strip()
    username = request.query_params.get('username').strip()
    
    password = form.cleaned_data.get('password')
    D0 = form.cleaned_data.get('D0')
    D1 = form.cleaned_data.get('D1')
    D2 = form.cleaned_data.get('D2')
    D3 = form.cleaned_data.get('D3')
    D4 = form.cleaned_data.get('D4')
    D5 = form.cleaned_data.get('D5')
    A0 = form.cleaned_data.get('A0')
    
    try:
        esp = Esp8266.objects.get(user__user__username=username, unique_id=unique_id)
        
        appliences = Applience.objects.filter(esp=esp).order_by("-id")
        appliences = AppliencesSerializer(appliences, many=True).data
    except:
        message = {"error": "404", "data": "Object not found !"}
        return Response(message)
    
    
    print(appliences)
    return Response(appliences)
    
        
    
    
    
    