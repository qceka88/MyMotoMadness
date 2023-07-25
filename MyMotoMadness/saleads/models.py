from django.db import models


# ADS FOR SALE MODELS
# Create your models here.
class Motorcycles(models.Model):
    bike_type = models.CharField(
        max_length=30,
        # choices  =  supersport, chopper, cross, etc,
    )
    brand = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=30,
    )
    engine_volume = models.PositiveIntegerField(

    )

    manufacture_year = models.PositiveIntegerField(
    )
    description = models.TextField(
        max_length=500,
    )
    owner = models.CharField(
        max_length=15
    )
    price = models.FloatField(

    )


class MotoGear(models.Model):
    brand = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=30,
    )
    gear_type = models.CharField(
        max_length=15,
        # choices  =  gloves, boots, tracksuit, etc..
    )
    manufacture_year = models.PositiveIntegerField(
    )
    description = models.TextField(
        max_length=500,
    )
    owner = models.CharField(
        max_length=15
    )
    price = models.FloatField(

    )


class MotoParts(models.Model):
    type_of_part = models.CharField(
        max_length=30,
        # choices  = engine, tyres, el system etc,
    )
    brand = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=30,
    )
    manufacture_year = models.PositiveIntegerField(
    )
    description = models.TextField(
        max_length=500,
    )
    owner = models.CharField(
        max_length=15
    )
    price = models.FloatField(

    )
