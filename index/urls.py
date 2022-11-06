from django.urls import path

from .views import home, esp_detail, update_applience

app_name= 'index'

urlpatterns = [
    path('home/', home, name='home'),
    path('esp/<str:uqid>', esp_detail, name='detail-esp'),
    path('applience/update/<int:pk>', update_applience, name='update-appl'),
    path('home/', home, name='home'),
    path('home/', home, name='home'),
    path('home/', home, name='home'),
]