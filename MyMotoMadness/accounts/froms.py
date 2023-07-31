from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class MotoUserRegisterForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password'
            }
        )
    )

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your username'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your email'
                }
            ),
        }


class MotoUserLoginForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your username'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter your password'
            }
        )
    )
