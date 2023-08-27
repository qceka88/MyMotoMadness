from django import forms
from django.contrib.auth import get_user_model
from django.core import exceptions

from MyMotoMadness.messagebox.models import MyMessage

UserModel = get_user_model()


class BaseMessageForm(forms.ModelForm):
    class Meta:
        model = MyMessage
        fields = (
            'message_subject',
            'message_content',
        )
        widgets = {
            'message_subject': forms.TextInput(
                attrs={
                    'placeholder': 'Message Subject',
                },
            ),
            'message_content': forms.Textarea(
                attrs={
                    'placeholder': 'Message Content',
                },
            ),
        }


class SendMessageForm(BaseMessageForm):
    ...


class CreateMessageForm(BaseMessageForm):
    input_user = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Username',
            }
        )

    )
    field_order = ('input_user', 'message_subject', 'message_content',)

    def clean(self):
        try:
            recipient = UserModel.objects.get(username=self.data['input_user'])
        except exceptions.ObjectDoesNotExist:
            recipient = ''
        if not recipient:
            raise exceptions.ValidationError(
                {'input_user': 'User not exist!'}
            )

        return self.cleaned_data
