from django import forms
from django.contrib.auth import get_user_model

from MyMotoMadness.messagebox.models import MyMessage

UserModel = get_user_model()


class BaseMessageForm(forms.ModelForm):
    class Meta:
        model = MyMessage
        fields = (
            'message_subject',
            'message_content',
        )


class CreateMessageForm(BaseMessageForm):
    ...
