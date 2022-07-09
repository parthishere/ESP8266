from enum import unique
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

from index.api.serializers import AppliencesSerializer
from .models import Applience, Esp8266, User, UserProfile
from .forms import SaveForm

from rest_framework.decorators import api_view

# Create your views here.

@csrf_exempt
@api_view(["GET", "POST"])
def home_view(request):
    led1 = None
    led2 = None
    led3 = None
    led4 = None
    pot = None
    
    context = { }
        
    if request.method == 'GET':
        print("GET :")
        uqid = str(request.GET.get('uqid', "")).strip()
        username = str(request.GET.get('username', "")).strip()
        
        print(username)
        user = User.objects.get(username=username)
        print(user)
        
        esp = Esp8266.objects.get(unique_id=uqid, user__user = user)
        print(esp)
        appliences = Applience.objects.filter(esp=esp).order_by('-id')
        print(appliences)
        # AppliencesSerializer(appliences, many=True)
        return Response(AppliencesSerializer.data)
    
    if request.method == 'POST':
        print("Post request and post data: ")

        data = SaveForm(request.POST)
        print(data.is_valid())
        print(data.cleaned_data)
        username = data.cleaned_data.get('username')
        user = User.objects.get(username=username)
        print(user)
        esp = Esp8266.objects.get(user__user = user)
        
        print(esp)
        payload = json.dumps({"led1":"ON", "led2": "OFF"})
        return Response(payload)
    
    
    return render(request, 'index/index.html', context=context)