from .views import (
    UserDestroyAPIView,
    UserRetriveUpdateAPIView,
    ListUsersAPI,
)

from django.urls import path


app_name = 'index-api'

urlpatterns = [


    
    path('user/<int:pk>/delete', UserDestroyAPIView.as_view(), name='delete-user'),
    path('user/<int:pk>', UserRetriveUpdateAPIView.as_view(), name='retrive-update-create-user'),
    path('user/list', ListUsersAPI.as_view(), name='list-user'),
    
]