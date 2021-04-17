from django.db.models.signals import post_save
from django.dispatch import receiver

from device_sensor.models import Device, Sensor


@receiver(post_save, sender=Device)
def create_sensors(sender, instance=None,
                                   created=False, **kwargs):

    if created:
        Sensor.objects.create(device=instance,sensor_type=Sensor.SensorType.TEMPERATURE_SENSOR.value)
        Sensor.objects.create(device=instance,sensor_type=Sensor.SensorType.PRESSURE_SENSOR.value)
