from django.contrib import admin

# Register your models here.
from .models import Esp8266, ChangeTime, Applience

admin.site.register(Esp8266)
admin.site.register(ChangeTime)
admin.site.register(Applience)