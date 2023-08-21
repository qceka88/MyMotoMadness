from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model, password_validation

UserModel = get_user_model()


class MotoUserChangePassword(auth_forms.PasswordChangeForm):
    old_password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "current-password",
                'placeholder': 'Enter your old password',
                'style': "height: 55px",
            }
        ),
    )
    new_password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            "autocomplete": "new-password",
            'placeholder': 'Enter your new password',
            'style': "height: 55px",
        }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'placeholder': 'New password confirmation',
                'style': "height: 55px",
            }
        ),
    )


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
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']
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
            'profile_picture': forms.HiddenInput(),
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
