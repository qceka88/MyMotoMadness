from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from MyMotoMadness.messagebox.models import MyMessage
from core.email_utils import send_the_email
from MyMotoMadness import settings



@receiver(post_save, sender=MyMessage)
def user_created(instance, created, **kwargs):
    if created:
        print('sended')
        #TODO: send email for received message
