from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from MyMotoMadness.saleads.mixins import BikeTypeChoices, ProtectionGearTypeChoices

UserModel = get_user_model()


class Motorcycles(models.Model):
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
        validators=(
            validators.MinValueValidator(1900),
            validators.MaxValueValidator(2023)
        )
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    price = models.FloatField(
    )
    city = models.CharField(
        max_length=30,
    )
    approved = models.BooleanField(
        default=False,
    )
    published = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.brand} {self.model} {self.engine_volume}"


class MotorcycleImages(models.Model):
    sale_ad = models.ForeignKey(
        Motorcycles,
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
        validators=(
            validators.MinValueValidator(1900),
            validators.MaxValueValidator(2023)
        )
    )
    description = models.TextField(
        max_length=500,
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    price = models.FloatField(

    )
    city = models.CharField(
        max_length=30,
    )
    approved = models.BooleanField(
        default=False,
    )
    published = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'{self.gear_type}, {self.brand}, {self.model} - {self.price:.2f}lv.'


class MotoEquipmentImages(models.Model):
    sale_ad = models.ForeignKey(
        to=MotoEquipmentGear,
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
        null=True,
        blank=True,
    )
    manufacture_year = models.PositiveIntegerField(
        validators=(
            validators.MinValueValidator(1900),
            validators.MaxValueValidator(2023)
        )
    )
    description = models.TextField(
        max_length=500,
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    price = models.FloatField(
    )
    city = models.CharField(
        max_length=30,
    )
    approved = models.BooleanField(
        default=False,
    )
    published = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"No{self.pk} - {self.type_of_part}, {self.brand}, {self.model}: {self.price:.2f}lv."


class MotoPartsImages(models.Model):
    sale_ad = models.ForeignKey(
        MotoParts,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='photos/part_photos',
    )
