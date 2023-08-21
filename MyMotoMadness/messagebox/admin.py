from django.contrib import admin

from MyMotoMadness.messagebox.models import MyMessage


# Register your models here.
@admin.register(MyMessage)
class MessageBoxAdmin(admin.ModelAdmin):
    ...
