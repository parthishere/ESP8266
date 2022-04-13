from .views import PostDataFromEsp, show_data_of_esp

from django.urls import path


app_name = 'index-api'

urlpatterns = [

    path('send-data', PostDataFromEsp.as_view(), name='return-data'),
    path('<str:mac>', show_data_of_esp, name='show-data')
]