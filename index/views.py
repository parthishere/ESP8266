from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
    

from .models import Esp8266


# Create your views here.

def home_view(request):
    led1 = None
    led2 = None
    led3 = None
    led4 = None
    pot = None
    
    context = { }
        
    if request.method == 'GET':
        return HttpResponse("i got get request")
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        led1 = request.POST.get('status')
        led2 = request.POST.get('station')
        led3 = request.POST.get('led1')
        led4 = request.POST.get('led1')
        pot = request.POST.get('led1')
        mac = request.POST.get('mac')
        mac_unhashed = request.POST.get('mac')
        print('mac')
        
        # esp_obj = Esp8266.objects.create(mac=mac, mac_unhashed=mac)
        # esp_obj.led1 = led1
        # esp_obj.led2 = led2
        # esp_obj.led3 = led3
        # esp_obj.led4 = led4
        # esp_obj.pot = pot
        
        context['led1'] = led1
        context['led2'] = led2
        context['led3'] = led3
        context['led4'] = led4
        context['mac'] = mac
        
        # esp_obj.save()
        
        # context['object'] = esp_obj
        print("hii")
        return HttpResponse("i got post data", led1, led2, led3, led4, pot, mac)
    
    
    return render(request, 'index/index.html', context=context)