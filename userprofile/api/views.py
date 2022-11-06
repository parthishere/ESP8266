from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import User, UserProfile
from .serializer import UserSerializer, UserProfileSerializer

class ListUsersAPI(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    
class UserRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    lookup_fields = ['pk']
     
    def get_object(self):
        queryset = self.get_queryset().filter(esp__user=self.request.user.user_profile)
        obj = queryset.get(pk=self.kwargs['pk'])
        return obj
    
    def perform_update(self, serializer):
        if self.request.user == serializer.validated_data.pop('user'):
            serializer.save(user=self.request.user)
        return super().perform_update(serializer)
               
class UserDestroyAPIView(DestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_destroy(self, instance):
        if self.request.user == instance.user:
            instance.delete()