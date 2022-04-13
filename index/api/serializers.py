from rest_framework import serializers

from index.models import Esp8266

from hashid_field import HashidField

class EspSerializer(serializers.ModelSerializer):
    # mac = HashidField(null=True, blank=True)
    class Meta:
        model = Esp8266
        exclude = ['mac']
        
    # def create(self, validated_data):
    #     Esp8266.objects.create(pot=validated_data['pot'])
    #     pass