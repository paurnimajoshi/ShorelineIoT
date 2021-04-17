from enum import Enum

from django.db import models

# Create your models here.

class Device(models.Model):
    unique_id = models.AutoField(primary_key=True)
    device_name = models.CharField(max_length=100,null=True,blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'device'

class Sensor(models.Model):

    class SensorType(Enum):
        TEMPERATURE_SENSOR = 1
        PRESSURE_SENSOR = 2

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    unique_id = models.AutoField(primary_key=True)
    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    sensor_type = models.CharField(null=True, max_length=50, choices=SensorType.as_tuple(), default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sensor'


class SensorData(models.Model):

    device = models.ForeignKey(Device,on_delete=models.CASCADE)
    sensor = models.ForeignKey(Sensor,on_delete=models.CASCADE)
    data = models.CharField(max_length=100,null=True,blank=True,default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sensor_data'
