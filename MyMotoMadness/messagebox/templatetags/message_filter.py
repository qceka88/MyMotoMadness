from django import template

from MyMotoMadness.saleads.models import Motorcycles, MotoEquipmentGear, MotoParts

register = template.Library()

@register.filter
def new_message(value):
    print(value)
    return True


