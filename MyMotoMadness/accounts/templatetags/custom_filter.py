from django import template

from MyMotoMadness.saleads.models import Motorcycles, MotoEquipmentGear, MotoParts

register = template.Library()


@register.filter
def class_name_show(value):
    return value.__class__.__name__


@register.simple_tag
def not_approved_offers():
    not_approved = []
    for offer in (Motorcycles.objects.filter(approved=False),
                  MotoEquipmentGear.objects.filter(approved=False),
                  MotoParts.objects.filter(approved=False)):
        not_approved.append(offer)

    return offer
