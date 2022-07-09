from rest_framework import serializers

from index.models import Esp8266, Applience, ChangeTime

from hashid_field import HashidField

class EspSerializer(serializers.ModelSerializer):
    # mac = HashidField(null=True, blank=True)
    class Meta:
        model = Esp8266
        fields = "__all__"
        
    # def create(self, validated_data):
    #     Esp8266.objects.create(pot=validated_data['pot'])
    #     pass
    
    
class AppliencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applience
        fields = "__all__"
        depth = 3
        
class ChangeTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeTime
        fields = "__all__"