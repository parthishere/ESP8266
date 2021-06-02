from rest_framework import serializers

from index.models import Esp8266

class EspSerializer(serializers.Serializer):
    class Meta:
        model = Esp8266
        fields = '__all__'
        
    # def create(self, validated_data):
    #     Esp8266.objects.create(pot=validated_data['pot'])
    #     pass