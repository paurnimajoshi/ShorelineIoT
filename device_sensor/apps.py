from django.apps import AppConfig


class DeviceSensorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'device_sensor'

    def ready(self):
        import device_sensor.signals
