from django.shortcuts import get_object_or_404
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
from .serializers import AppliencesSerializerESP, EspSerializerESP, AppliencesSerializer, EspSerializer


@api_view(['GET'])
def return_data_to_esp_view(request):
    message = {}
    username = request.query_params.get('username')
    unique_id = request.query_params["uqid"]
    
    unique_id.replace(" ", "")
    uqid = ""
    for a in unique_id:
        if a == '\0' or a == "" or len(a) == 0:
            pass
        else:
            uqid += a

    try:
        esp = Esp8266.objects.get(user__user__username=username, unique_id=uqid)
        
        appliences = Applience.objects.filter(esp=esp).order_by("-id")
    except:
        message = {"error": "404", "data": "Object not found !"}
        return Response(message)
    
    serializer = AppliencesSerializerESP(appliences, many=True)
    print(Response(serializer.data))
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
    
    unique_id.replace(" ", "")
    uqid = ""
    for a in unique_id:
        if a == '\0' or a == "" or len(a) == 0:
            pass
        else:
            uqid += a
    
    password = form.cleaned_data.get('password')
    D0 = form.cleaned_data.get('D0')
    D1 = form.cleaned_data.get('D1')
    D2 = form.cleaned_data.get('D2')
    D3 = form.cleaned_data.get('D3')
    D4 = form.cleaned_data.get('D4')
    D5 = form.cleaned_data.get('D5')
    A0 = form.cleaned_data.get('A0')
    
    try:
        esp = Esp8266.objects.get(user__user__username=username, unique_id=uqid)
        
        appliences = Applience.objects.filter(esp=esp).order_by("-id")
        appliences = AppliencesSerializerESP(appliences, many=True).data
    except:
        message = {"error": "404", "data": "Object not found !"}
        return Response(message)
    
    
    print(appliences)
    return Response(appliences)
    
        
        
        

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
    
    
    
class ESPListCreateAPI(ListCreateAPIView):
    queryset = Esp8266.objects.all()
    serializer_class = EspSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = ['unique_id']
    lookup_url_kwarg = ['unique_id']
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def list(self, request):
        queryset = self.get_queryset().filter(user=request.user.user_profile)
        serializer = EspSerializer(queryset, many=True)
        return Response(serializer.data)
    
class ESPRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Esp8266.objects.all()
    serializer_class = EspSerializer
    permission_classes = [IsAuthenticated]
    
    
    def perform_update(self, serializer):
        instance = serializer.save(user=self.request.user.user_profile)
               
class ESPDestroyAPIView(DestroyAPIView):
    queryset = Esp8266.objects.all()
    serializer_class = EspSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        if self.request.user == instance.user.user:
            instance.delete()
            
            
            
            
            
class ListCreateAppliencesAPI(ListCreateAPIView):
    queryset = Applience.objects.all()
    serializer_class = AppliencesSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['unique_id', 'pk']
    
    def list(self, request):
        user = request.user
        queryset = self.get_queryset().filter(esp__user=user.user_profile)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class AppliencesRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Applience.objects.all()
    serializer_class = AppliencesSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['pk']
     
    def get_object(self):
        queryset = self.get_queryset().filter(esp__user=self.request.user.user_profile)
        obj = queryset.get(pk=self.kwargs['pk'])
       
        return obj
               
class AppliencesDestroyAPIView(DestroyAPIView):
    queryset = Applience.objects.all()
    serializer_class = AppliencesSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        if self.request.user == instance.esp.user.user:
            instance.delete()
        
        
        
        
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
   

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
    