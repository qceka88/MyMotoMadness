from django.contrib import admin

from MyMotoMadness.saleads.models import MotoEquipmentGear, MotoParts, Motorcycles


@admin.register(Motorcycles)
class MotorcyclesAdmin(admin.ModelAdmin):
    ...


@admin.register(MotoEquipmentGear)
class MotoGearAdmin(admin.ModelAdmin):
    ...


@admin.register(MotoParts)
class MotoPartsAdmin(admin.ModelAdmin):
    ...
