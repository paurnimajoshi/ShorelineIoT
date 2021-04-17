from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^create/device/', views.CreateDevices.as_view(), name='create_device'),
    url(r'^update/device/', views.CreateDevices.as_view(), name='update_device'),
    url(r'^create/sensor/data/', views.CreateSensorData.as_view(), name='create_sensordata'),
    url(r'^get/sensor/data/', views.GetSensorData.as_view(), name='create_sensordata'),
]
