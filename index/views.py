from enum import unique
import re
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

from index.api.serializers import AppliencesSerializer
from .models import Applience, Esp8266, User, UserProfile
from .forms import SaveForm

from rest_framework.decorators import api_view

# Create your views here.
@login_required(login_url="accounts:login")
def home(request):
    context = {}
    user =request.user
    
    esps = Esp8266.objects.filter(user__user=user)
    
    applieneces = []
    for esp in esps:
        applienece = Applience.objects.filter(esp=esp)
        applieneces.append(applienece)
        
    context['esps'] = esps
    context['applieneces'] = applieneces
    return render(request, "index/home.html", context)

@login_required(login_url="accounts:login")
def esp_detail(request, uqid):
    context = {}
    
    user =request.user
    esp = Esp8266.objects.get(unique_id=uqid)
    
    context['esp'] = esp
    context['applieneces'] = Applience.objects.filter(esp=esp)
    return render(request, 'index/esp-detail.html', context)


def update_applience(request, pk=None):
    context = {}
    if request.POST:
        user = request.user
        appliance = Applience.objects.get(pk=pk)
    return render(request, '', context)


def profile(request):
    context  = {}
    return render(request, "index/profile.html", context)

def update_profile(request):
    context  = {}
    return render(request, "profile.html", context)

def update_esp(request):
    context  = {}
    return render(request, "profile.html", context)

def delete_esp(request):
    return redirect("index:home")

