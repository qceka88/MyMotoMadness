from django.contrib import admin

from MyMotoMadness.saleads.models import MotoEquipmentGear, MotoParts, Motorcycles


@admin.register(Motorcycles)
class MotorcyclesAdmin(admin.ModelAdmin):
    list_display = ('bike_type', 'brand', 'model', 'engine_volume', 'manufacture_year', 'price', 'owner')
    ordering = ('published', 'brand', 'model', 'manufacture_year')
    list_filter = ('bike_type', 'brand', 'model', 'engine_volume', 'manufacture_year', 'price', 'owner')
    search_fields = ('bike_type', 'brand', 'model', 'engine_volume', 'manufacture_year', 'price', 'owner')


@admin.register(MotoEquipmentGear)
class MotoGearAdmin(admin.ModelAdmin):
    list_display = ('gear_type', 'brand', 'model', 'material_type', 'manufacture_year', 'price', 'owner')
    ordering = ('published', 'brand', 'model', 'manufacture_year')
    list_filter = ('gear_type', 'brand', 'model', 'material_type', 'price', 'owner')
    search_fields = ('gear_type', 'brand', 'model', 'material_type', 'price', 'owner')


@admin.register(MotoParts)
class MotoPartsAdmin(admin.ModelAdmin):
    list_display = ('type_of_part', 'brand', 'model', 'for_bike', 'price', 'owner')
    ordering = ('published', 'brand', 'model', 'manufacture_year')
    list_filter = ('type_of_part', 'brand', 'model', 'for_bike', 'price', 'owner')
    search_fields = ('type_of_part', 'brand', 'model', 'for_bike', 'price', 'owner')
