from django.contrib import admin

from MyMotoMadness.accounts.models import MotoUserModel


# Register your models here.
@admin.register(MotoUserModel)
class MotoUserAdmin(admin.ModelAdmin):
    fields = ['name_last', 'name_first', 'email', 'profile_image']
