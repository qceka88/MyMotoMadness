from django.db import models

from MyMotoMadness.saleads.model_mixins import BikeTypeChoices, ProtectionGearTypeChoices


# ADS FOR SALE MODELS
# TODO: Add object in Owner in all models
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
    horse_power = models.IntegerField(

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

    approved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.brand} {self.model} {self.engine_volume}"


class MotorcycleImages(models.Model):
    motorcycle = models.ForeignKey(
        MotorcyclesModel,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='photos/bike_photos',
    )


class MotoEquipmentGear(models.Model):
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
    approved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.gear_type}, {self.brand}, {self.model} - {self.price:.2f}lv.'


class MotoEquipmentImages(models.Model):
    moto_equipment = models.ForeignKey(
        MotoEquipmentGear,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='photos/equipment_photos',
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
    for_bike = models.CharField(
        max_length=40,
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
    approved = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f"{self.type_of_part}, {self.brand}, {self.model}: {self.price:.2f}lv."

class MotoPartsImages(models.Model):
    moto_parts = models.ForeignKey(
        MotoParts,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='photos/part_photos',
    )
