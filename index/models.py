from django.db import models

from hashid_field import HashidField


class Esp8266Manager(models.Manager):
    def get_or_new(self, mac=None):
        qs = self.get_queryset().filter(mac_unhashed=mac)
        
        if qs.exists():
            obj = qs.first()
        else:
            obj = self.new(mac=mac)
            
    def new(self, mac=None):
        obj = self.model.objects.create(mac_unhashed=mac)
        return obj
        
        

class Esp8266(models.Model):
    led1 = models.BooleanField(default=False)
    led2 = models.BooleanField(default=False)
    led3 = models.BooleanField(default=False)
    led4 = models.BooleanField(default=False)
    pot  = models.IntegerField(default=0)
    mac  = HashidField(null=True, blank=True)
    mac_unhash = models.CharField(null=True, blank=True, max_length=50)
    updated = models.DateTimeField(auto_now=True)
    
    objects = Esp8266Manager()
    
    def __str__(self):
        return str(self.pk)