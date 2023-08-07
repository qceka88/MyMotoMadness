from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class MotoUserRegisterForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'style': "height: 55px",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repeat the password',
                'style': "height: 55px",
            }
        ),
    )

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your username',
                    'style': "height: 55px",
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your email',
                    'style': "height: 55px",
                }
            ),
        }


class MotoUserLoginForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your username',
                'style': "height: 55px",

            }
        ),
        label='',

    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password',
                'style': "height: 55px",
            }
        ),
        label='',
    )
