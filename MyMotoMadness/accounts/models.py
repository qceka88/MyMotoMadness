from django.contrib.auth import models as auth_models
from django.db import models


# ACCOUNTS MODELS.
class MotoUserModel(auth_models.AbstractUser):
    first_name = models.CharField(
        max_length=30,
    )
    # TODO: To add name alphabet validator
    last_name = models.CharField(
        max_length=30,
    )
    email = models.EmailField(
        unique=True,
    )
    profile_picture = models.ImageField(
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        max_length=15,
    )

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
