from django.contrib import admin

from MyMotoMadness.saleads.models import MotoEquipmentGear, MotoParts, MotorcyclesModel


# Register your models here.


@admin.register(MotoEquipmentGear)
class MotoGearAdmin(admin.ModelAdmin):
    ...


@admin.register(MotoParts)
class MotoPartsAdmin(admin.ModelAdmin):
    ...


@admin.register(MotorcyclesModel)
class MotorcyclesAdmin(admin.ModelAdmin):
    ...
