from django.contrib import admin
from .models import Log, Weather

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    pass

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    pass
