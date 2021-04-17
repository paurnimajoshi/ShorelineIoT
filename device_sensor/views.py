import logging
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from ShorelineIoT import error_conf
from device_sensor.models import Device, Sensor, SensorData
from device_sensor.serializer import CreateDeviceSerializer, CreateSensorDataSerializer

logging = logging.getLogger('log')


class CreateDevices(APIView):
    """
    API to create Device data
    """
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            data = request.data
            logging.info("....request data - create device data....: "+str(data))
            serializer = CreateDeviceSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error("....Exception create device data....: "+str(e))
            return Response({e},status==status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        try:
            data = request.data
            logging.info("....request data - update device data....: "+str(data))
            ext_device = Device.objects.get(unique_id = data.get("unique_id"))
            ext_device.device_name = data.get("device_name")
            ext_device.save()
            serializer = CreateDeviceSerializer(ext_device)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            logging.error("....Exception update device data....: "+str(e))
            return Response(error_conf.DEVICE_NOT_FOUND,status==status.HTTP_400_BAD_REQUEST)


class CreateSensorData(APIView):
    """
    API to Update Sensor data
    """
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            data = request.data
            logging.info("....request data - update sensor data....: "+str(data))
            ext_sensor = Sensor.objects.get(unique_id=data.get("unique_id"))
            data['device'] = ext_sensor.device.unique_id
            data['sensor'] = ext_sensor.unique_id
            serializer = CreateSensorDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logging.error("....Exception in update sensor data....: "+str(e))
            return Response(error_conf.SENSOR_NOT_FOUND,status=status.HTTP_400_BAD_REQUEST)


class GetSensorData(ListAPIView):
    """
    API to get Sensor data
    """
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            data = request.data
            logging.info("....request data - get sensor data....: "+str(data))
            sensor_data = SensorData.objects.filter(sensor__sensor_type=data.get("sensor_type"),created_at__range=(data.get("from_date"),data.get("to_date")))
            serializer = CreateSensorDataSerializer(sensor_data,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            logging.error("....Exception in get sensor data....: "+str(e))
            return Response({},status=status.HTTP_400_BAD_REQUEST)
