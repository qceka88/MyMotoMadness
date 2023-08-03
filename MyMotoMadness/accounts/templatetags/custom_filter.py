from django import template

register = template.Library()


@register.filter
def class_name_show(value):
    return value.__class__.__name__
