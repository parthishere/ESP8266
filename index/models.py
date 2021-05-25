from django.db import models

class Esp8266(models.Model):
    led1 = models.BooleanField(default=False)
    led2 = models.BooleanField(default=False)
    led3 = models.BooleanField(default=False)
    led4 = models.BooleanField(default=False)
    pot  = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.pk