from .views import return_data_to_esp_view, get_posted_data_from_esp

from django.urls import path


app_name = 'index-api'

urlpatterns = [

    path('get/', return_data_to_esp_view, name='return-data'),
    path('post/', get_posted_data_from_esp, name='show-data')
]