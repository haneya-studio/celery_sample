from django.db import models


class Log(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAIL = 'failed'
    STATUS_SET = (
      (STATUS_OK, "正常"),
      (STATUS_FAIL, "失敗"),
    )
    read_at = models.DateTimeField(auto_now_add=True)
    target = models.CharField(max_length=24)
    status = models.CharField(max_length=10)

    def __repr__(self):
        return "{}: {}: {}".format(self.pk, self.target, self.read_at)

    __str__ = __repr__


class Weather(models.Model):
    read_at = models.DateTimeField(auto_now_add=True)
    pred_date = models.DateField()
    place1 = models.CharField(max_length=6)
    place2 = models.CharField(max_length=6)
    place3 = models.CharField(max_length=6)
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    rain_rate = models.IntegerField()
    weather = models.CharField(max_length=6)
    confidence = models.CharField(max_length=6, null=True, blank=True)
    weather_clear = models.FloatField()
    weather_sunny = models.FloatField()
    weather_cloudy = models.FloatField()
    weather_rainy = models.FloatField()
    weather_snow = models.FloatField()
    weather_blizzard = models.FloatField()
    weather_typhoon = models.FloatField()
    cloud_duration = models.FloatField()
    rain_duration = models.FloatField()
    sunny_duration = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



