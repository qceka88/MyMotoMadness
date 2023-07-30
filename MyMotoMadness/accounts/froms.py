from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class MotoUserRegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
