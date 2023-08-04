from django.contrib import admin

from MyMotoMadness.accounts.models import MotoUserModel


# Register your models here.
@admin.register(MotoUserModel)
class MotoUserAdmin(admin.ModelAdmin):
    fields = ('first_name',
              'last_name',
              'email',
              'profile_picture',
              'phone_number',
              'is_staff',
              'is_superuser',
              'groups')
