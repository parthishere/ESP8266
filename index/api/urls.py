from .views import PostDataFromEsp

from django.urls import path


app_name = 'index-api'

urlpatterns = [

    path('', PostDataFromEsp.as_view(), name='home-api')
]