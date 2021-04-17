from django.contrib import admin

# Register your models here.
from device_sensor.models import Device, Sensor

admin.site.register(Device)
admin.site.register(Sensor)

