from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_frmaework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

import datetime

from rest_framework.decorators import api_view


from index.models import Esp8266
from .serializers import EspSerializer

# class EspDataListAPIView(generics.ListAPIView):
#     queryset = Esp8266.objects.all()
#     serializer_class = EspSerializer
#     permission_classes = [IsAdminUser]
    
#     def post()

def get_data_from_esp(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]
    
    def post(self, request, format=None):
        mac = request.POST.get('mac')
        try:
            led1 = request.POST.get('led1')
        except Exception as e:
            print(e)
            led1=None
        
            
        try:
            led2 = request.POST.get('led2')
        except Exception as e:
            print(e)
            led2=None
        
            
        try:
            led3 = request.POST.get('led3')
        except Exception as e:
            print(e)
            led3=None
            
            
        try:
            pot = request.POST.get('pot')
        except Exception as e:
            print(e)
            pot=None
            
        obj = Esp8266.objects.create(mac=mac, led1=led1, led2=led2, led3=led3, pot=pot)
        
        return_data_to_esp(request, mac=mac)
        
        return Response({ 'object': obj })
    
            
    

    
    
@api_view(['GET'])
def return_data_to_esp(request, mac):
    
    def get(self, request, format=None):
        try:
            qs=Esp8266.objects.filter(mac_id=mac,
                                        timestamp__gte=(datetime.datetime.now() - datetime.timedelta(minutes=15))
                                        )
        except:
            return Response({'Error':True,'Cause':'No Data for this sensor at this time'})
        data = {
            'objects_list': qs,
        }
        return Response(data)