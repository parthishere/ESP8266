from ..models import User, UserProfile
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        exclude = ('password')



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserProfile
        fields = '__all__'
