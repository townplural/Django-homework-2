from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor')
    temperature = models.IntegerField()
    created_at = models.DateTimeField()
