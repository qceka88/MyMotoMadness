from django.db.models.signals import post_save
from django.dispatch import receiver

from MyMotoMadness import settings
from MyMotoMadness.messagebox.models import MyMessage
from core.email_utils import send_the_email


def message_notification_with_email(user_sender, user_receiver, data):
    context = {
        'user_sender': user_sender,
        'user_receiver': user_receiver,
        'message_subject': data.message_subject,
        'message_slug': f"{user_sender.username.lower()}-{user_receiver.username.lower()}-{data.pk}",

    }
    return send_the_email(
        subject=f'You have new message from {user_sender}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user_receiver.email,),
        template_name='emails/message_notification.html',
        context=context,
    )


@receiver(post_save, sender=MyMessage)
def message_send(instance, created, **kwargs):
    if created:
        message_notification_with_email(instance.from_user, instance.to_user, instance)
