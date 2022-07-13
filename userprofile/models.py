from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save

import random
import string

# Create your models here.
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
        new_slug = "{}-{randstr}".format(
                    randstr=random_string_generator(size=12)
                )
        return new_slug
    else:
        return new_id


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    unique_id = models.CharField(null=True, blank=True, max_length=120) 
    
def user_post_save_reciever(sender, instance, *args, **kwargs):
    pass


post_save.connect(user_post_save_reciever, sender=User)