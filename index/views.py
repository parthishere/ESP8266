from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Esp8266
from .forms import SaveForm

# Create your views here.

@csrf_exempt
def home_view(request):
    led1 = None
    led2 = None
    led3 = None
    led4 = None
    pot = None
    
    context = { }
        
    if request.method == 'GET':
        print("GET :")
        print(request.GET.get('uqid'))
        print(request.GET.get('username'))
        
        return HttpResponse("i got get request")
    
    if request.method == 'POST':
        print("Post request and post data: ")
        print(request.GET.get('uqid'))
        print(request.GET.get('username'))

        data = SaveForm(request.POST)
        print(data.is_valid())
        print(data.cleaned_data)
        
        
        payload = json.dumps({"led1":"ON", "led2": "OFF"})
        return HttpResponse(payload)
    
    
    return render(request, 'index/index.html', context=context)