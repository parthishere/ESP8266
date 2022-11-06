from rest_framework import serializers

from index.models import Esp8266, Applience, ChangeTime

from hashid_field import HashidField


class EspSerializer(serializers.ModelSerializer):
    # mac = HashidField(null=True, blank=True)
    class Meta:
        model = Esp8266
        exclude = ['user',]
        
    def create(self, validated_data):
        
        count = Esp8266.objects.filter(user=user_profile).count()
        if count > 4:
            pass
        else:
            Esp8266.objects.create(**validated_data)

class AppliencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applience
        fields = "__all__"
        depth = 3
        
    def create(self, validated_data):
        esp=validated_data.get('esp')
        count = Applience.objects.filter(esp=esp).count()
        if count > 6:
            pass
        else:
            Applience.objects.create(**validated_data)
            
    def update(self, instance, validated_data):
        esp = validated_data.pop('esp')
        return super().update(instance, validated_data)



class EspSerializerESP(serializers.ModelSerializer):

    class Meta:
        model = Esp8266
        exclude = ['user', 'timestamp']

    
    
class AppliencesSerializerESP(serializers.ModelSerializer):
    esp = EspSerializer()
    class Meta:
        model = Applience
        fields = ['esp', 'name', 'value']
        
    def create(self, validated_data):
        esp=validated_data.get('esp')
        count = Applience.objects.filter(esp=esp).count()
        if count > 6:
            pass
        else:
            Applience.objects.create(**validated_data)
            
    def update(self, instance, validated_data):
        esp = validated_data.pop('esp')
        return super().update(instance, validated_data)
      
  
class ChangeTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeTime
        fields = "__all__"