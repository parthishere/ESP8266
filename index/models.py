from django.db import models
from datetime import timezone

from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save

from userprofile.models import UserProfile

import random
import string




def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_id_generator(instance):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
        """
    new_id = random_string_generator(size=12)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(unique_id=new_id).exists()
    print(instance.__class__)
    if qs_exists:
        new_slug = "esp-{randstr}".format(
                    randstr=random_string_generator(size=12)
                )
        return new_slug
    else:
        return new_id


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
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='esps')
    unique_id = models.CharField(null=True, blank=True, max_length=120) 
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    objects = Esp8266Manager()
    
    def __str__(self):
        return f"esp {str(self.pk)}"
    
    
class Applience(models.Model):
    esp = models.ForeignKey(Esp8266, on_delete=models.CASCADE, related_name='appliences')
    boolean = models.BooleanField(default=True)
    name = models.CharField(default='led', max_length=120)
    value = models.IntegerField(default='0', null=True, blank=True)
    unique_id = models.CharField(null=True, blank=True, max_length=120) 
    
    def __str__(self):
        return str(f"applience of {self.esp.unique_id}")
    
    
class ChangeTime(models.Model):
    Appliences = models.ForeignKey(Applience, on_delete=models.CASCADE, related_name='updates')
    updated_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return str("applience of {self.esp.unique_id}")
    
def user_post_save_receiver(sender, instance, *args, **kwargs):
    obj = Esp8266.objects.get(user=instance)
    if obj is None:
        Esp8266.objects.create(user=instance)
    else:
        pass

post_save.connect(User, user_post_save_receiver)


def applience_post_save_receiver(sender, instance, *args, **kwargs):
    esp = instance.esp
    count = Applience.objects.filter(esp=esp).count()
    if count > 6:
        return 
    if instance.boolean == True:
        if instance.value>0:
            instance.value=0
    instance.save()
    
post_save.connect(Applience, applience_post_save_receiver)
    
    
    
    
