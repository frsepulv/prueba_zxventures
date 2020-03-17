from django.contrib.gis.db import models

# Create your models here.

class Provider(models.Model):
    id = models.IntegerField(primary_key=True)
    tradingName = models.CharField(max_length=64)
    ownerName = models.CharField(max_length=64)
    document = models.CharField(max_length=32, unique=True)
    coverageArea = models.MultiPolygonField()
    address = models.PointField()
