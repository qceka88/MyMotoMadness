from django import template

register = template.Library()


@register.filter
def left_column(data):
    return [art for n,art in enumerate(data) if n % 2 != 0]


@register.filter
def right_column(data):
    return [art for n,art in enumerate(data) if n % 2 == 0]

