from django.db import models

from MyMotoMadness.saleads.model_mixins import BikeTypeChoices, ProtectionGearTypeChoices


# ADS FOR SALE MODELS
class MotorcyclesModel(models.Model):
    bike_type = models.CharField(
        max_length=30,
        choices=BikeTypeChoices.choices(),
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
        null=True,
        blank=True,
    )
    owner = models.CharField(
        max_length=15,
    )
    price = models.FloatField(

    )
    bike_image = models.ImageField(
        upload_to='bike_photos',
        blank=True,
        null=True,
    )
    approved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.brand} {self.model} {self.engine_volume}"


class MotoGear(models.Model):
    brand = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=30,
    )
    gear_type = models.CharField(
        max_length=20,
        choices=ProtectionGearTypeChoices.choices(),
    )

    material_type = models.CharField(
        max_length=30,
        null=True,
        blank=True,
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
    gear_image = models.ImageField(
        upload_to='gear_photos',
        blank=True,
        null=True,
    )
    approved = models.BooleanField(
        default=False,
    )


class MotoParts(models.Model):
    type_of_part = models.CharField(
        max_length=30,
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
    part_image = models.ImageField(
        upload_to='part_photos',
        blank=True,
        null=True,
    )
    approved = models.BooleanField(
        default=False,
    )
