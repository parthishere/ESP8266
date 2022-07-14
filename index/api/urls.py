from .views import (
    return_data_to_esp_view,
    get_posted_data_from_esp,
    
    ESPDestroyAPIView,
    ESPRetriveUpdateAPIView,
    ESPListCreateAPI,
    
    ListCreateAppliencesAPI,
    AppliencesDestroyAPIView,
    AppliencesRetriveUpdateAPIView
)

from django.urls import path


app_name = 'index-api'

urlpatterns = [

    path('get/', return_data_to_esp_view, name='return-data'),
    path('post/', get_posted_data_from_esp, name='show-data'),
    
    path('esp/<int:unique_id>/delete', ESPDestroyAPIView.as_view(), name='delete-esp'),
    path('esp/<int:unique_id>', ESPRetriveUpdateAPIView.as_view(), name='retrive-update-create-esp'),
    path('esp/list', ESPListCreateAPI.as_view(), name='list-esp'),
    
    path('appliences/list', ListCreateAppliencesAPI.as_view(), name='delete-applience'),
    path('appliences/<int:pk>/delete', AppliencesDestroyAPIView.as_view(), name='retrive-update-create-applience'),
    path('appliences/<int:pk>', AppliencesRetriveUpdateAPIView.as_view(), name='list-applience'),
]