from rest_framework import serializers

from device_sensor.models import Device, SensorData


class CreateDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class CreateSensorDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorData
        fields = '__all__'
