from django.db import models
from datetime import timezone

from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save

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
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    objects = Esp8266Manager()
    
    def __str__(self):
        return str(self.pk)
    
    
def user_post_save_receiver(sender, instance, *args, **kwargs):
    obj = Esp8266.objects.get(user=instance)
    if obj is None:
        Esp8266.objects.create(user=instance)
    else:
        pass

post_save.connect(User, user_post_save_receiver)
    
    
    
