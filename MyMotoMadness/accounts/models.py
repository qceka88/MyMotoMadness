from django.contrib.auth import models as auth_models
from django.db import models
from django.shortcuts import redirect
from django.template.defaultfilters import slugify

from MyMotoMadness.accounts.validators import check_name_symbols_for_non_alphabetical, phone_validator


class MotoUserModel(auth_models.AbstractUser):
    first_name = models.CharField(
        max_length=30,
        validators=(
            check_name_symbols_for_non_alphabetical,
        ),
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=30,
        validators=(
            check_name_symbols_for_non_alphabetical,
        ),
        null=True,
        blank=True,
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
        null=True,
        blank=True,
        validators=(phone_validator,)
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )

    def __str__(self):
        return f"{self.username}"

    def get_absolute_url(self):
        return redirect('edit user view', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.username}")

        return super().save(*args, **kwargs)
