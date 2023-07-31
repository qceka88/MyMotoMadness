from django.contrib.auth import forms as auth_forms, get_user_model
from django import  forms
UserModel = get_user_model()


class MotoUserRegisterForm(auth_forms.UserCreationForm):
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
            'password1': forms.PasswordInput(
                attrs={
                    'placeholder': 'Enter your password'
                }
            ),
            'password2': forms.PasswordInput(
                attrs={
                    'placeholder': 'Repeat  the password'
                }
            ),
        }


