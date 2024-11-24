from .models import Log, Weather
from rest_framework import viewsets, serializers


class LogSerializer(serializers.ModelSerializer):
  class Meta:
    model = Log
    fields = "__all__"


class LogViewSet(viewsets.ModelViewSet):
  queryset = Log.objects.all()
  serializer_class = LogSerializer


class WeatherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Weather
    fields = "__all__"


class WeatherViewSet(viewsets.ModelViewSet):
  queryset = Weather.objects.all()
  serializer_class = WeatherSerializer
