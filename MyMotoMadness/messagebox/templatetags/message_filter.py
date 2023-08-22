from django import template

from MyMotoMadness.messagebox.models import MyMessage

register = template.Library()


@register.filter
def new_message(user_object):
    for message in MyMessage.objects.filter(to_user=user_object, viewed=False):
        if message:
            return True
