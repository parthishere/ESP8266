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

# class EspDataListAPIView(generics.ListAPIView):
#     queryset = Esp8266.objects.all()
#     serializer_class = EspSerializer
#     permission_classes = [IsAdminUser]
    
#     def post()

class PostDataFromEsp(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    # def get(self, request):
    #     mac = self.mac
    #     try:
    #         qs=Esp8266.objects.filter(mac_id=mac,
    #                                     timestamp__gte=(datetime.datetime.now() - datetime.timedelta(minutes=15))
    #                                     )
    #     except:
    #         return Response({'Error':True,'Cause':'No Data for this sensor at this time'})
    #     obj = EspSerializer(qs, many=False)
    #     return Response(obj.data)
    
    def post(self, request, format=None):
        self.mac = request.POST.get('mac')
        user_id = request.POST.get('user_id')
        self.user = User.objects.get(id=self.user_id)
        
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
            
        
        print("led1 : ", request.POST.get('led1'))
        print("led2 : ", request.POST.get('led2'))
        print("led3 : ", request.POST.get('led3'))
        print("led4 : ", request.POST.get('led4'))
        
        obj = Esp8266.objects.filter(mac=self.mac, user=self.user)
        
        if obj is not None:

            obj.led1=led1
            obj.led2=led2
            obj.led3=led3
            obj.pot=pot
            
            obj.save()
        
            esp_obj = EspSerializer(obj, many=False)
            
            return Response(esp_obj.data)
        
        
        else:
            
            data = {
                    "status": 400,
                    "message": {
                        "error": f"No Object Found with requested Id and mac",
                    }
                }
            
            return Response(data)
    
            
    

    
    

# @login_required()
@api_view(['GET'])
def show_data_of_esp(request, mac):
    qs=Esp8266.objects.get(user=request.user, mac_unhash=mac)
    print(qs)
    if qs is None:
        return Response({'Error':True,'Cause':'No Data for this sensor at this time'})
    # data = {
    #     'objects_list': 
    # }
    print(EspSerializer(qs).data)
    return Response(EspSerializer(qs).data)
    # def get(self, request, format=None):
        