from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from weather.views import LogViewSet, WeatherViewSet

router = routers.DefaultRouter()
router.register(r'log', LogViewSet)
router.register(r'weather', WeatherViewSet)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include(router.urls)),
]

