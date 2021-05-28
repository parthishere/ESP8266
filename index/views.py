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
    
    if request.GET or request.POST:
        led1 = request.GET.get('led1')
        led2 = request.GET.get('led1')
        led3 = request.GET.get('led1')
        led4 = request.GET.get('led1')
        pot = request.GET.get('led1')
        mac = request.POST.get('mac')
        mac_unhashed = request.POST.get('mac')
        print('mac')
        
        esp_obj = Esp8266.objects.create(mac=mac, mac_unhashed=mac)
        esp_obj.led1 = led1
        esp_obj.led2 = led2
        esp_obj.led3 = led3
        esp_obj.led4 = led4
        esp_obj.pot = pot
        
        
        esp_obj.save()
        
        context['object'] = esp_obj
    
    
    return render(request, 'index/index.html', context=context)