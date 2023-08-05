from django.contrib.auth import models as auth_models
from django.db import models
from django.shortcuts import redirect

from MyMotoMadness.accounts.validators import check_name_symbols_for_non_alphabetical


# ACCOUNTS MODELS.
class MotoUserModel(auth_models.AbstractUser):
    first_name = models.CharField(
        max_length=30,
        validators=(
            check_name_symbols_for_non_alphabetical,
        ),
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            check_name_symbols_for_non_alphabetical,
        ),
    )
    email = models.EmailField(
        unique=True,
    )
    profile_picture = models.ImageField(
        upload_to='photos/profile_pictures',
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=15,
    )


    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return redirect('edit user view', kwargs={'pk': self.pk})
