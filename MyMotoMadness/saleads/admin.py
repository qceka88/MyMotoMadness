from django.contrib import admin

from MyMotoMadness.saleads.models import MotoGear, MotoParts, MotorcyclesModel


# Register your models here.


@admin.register(MotoGear)
class MotoGearAdmin(admin.ModelAdmin):
    ...


@admin.register(MotoParts)
class MotoPartsAdmin(admin.ModelAdmin):
    ...


@admin.register(MotorcyclesModel)
class MotorcyclesAdmin(admin.ModelAdmin):
    ...
