from django.contrib import admin

from MyMotoMadness.accounts.models import MotoUserModel


# Register your models here.
@admin.register(MotoUserModel)
class MotoUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    fields = ('first_name',
              'last_name',
              'email',
              'profile_picture',
              'phone_number',
              'is_staff',
              'is_superuser',
              'groups')
    ordering = ('username', 'first_name', 'last_name')
    list_filter = ['username', 'is_superuser', 'is_staff']
    search_fields = ('username', 'first_name', 'last_name', 'phone_number', 'is_superuser', 'is_staff')
