from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.email_utils import send_the_email
from MyMotoMadness import settings

UserModel = get_user_model()


def send_successful_registration_email(user):
    context = {
        'user': user,
    }
    return send_the_email(
        subject='Registration greetings!',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,),
        template_name='emails/email-greeting.html',
        context=context,
    )


@receiver(post_save, sender=UserModel)
def user_created(instance, created, **kwargs):
    if created:
        send_successful_registration_email(instance)
