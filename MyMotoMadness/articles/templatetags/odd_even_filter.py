from django import template

register = template.Library()


@register.filter
def odd_numbers(data):
    return [art for art in data if art.pk % 2 != 0]


@register.filter
def even_numbers(data):
    return [art for art in data if art.pk % 2 == 0]

