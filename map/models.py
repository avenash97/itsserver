from django.contrib.gis.db import models

# Create your models here.
class Farms(models.Model):
    farm_id = models.IntegerField()
    farm_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    area = models.IntegerField()
    region = models.CharField(max_length=50)
    farm_polygon = models.PolygonField()


class Household(models.Model):
    household_id = models.IntegerField()
    owner_name = models.CharField(max_length=50)
    income = models.IntegerField()
    location = models.PointField(null =True)
    no_of_members = models.IntegerField()


class Well(models.Model):
    well_id = models.IntegerField()
    owner_name = models.CharField(max_length=50)
    farm_associated = models.IntegerField()
    location = models.PointField(null =True)
    depth = models.FloatField()
    average_yield = models.FloatField()
