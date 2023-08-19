from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()


class MyMessage(models.Model):
    from_user = models.ForeignKey(
        UserModel,
        related_name='pk+',
        on_delete=models.CASCADE,
    )

    to_user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )

    message_subject = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    message_content = models.TextField(
        max_length=500,
    )

    send_date = models.DateTimeField(
        auto_now_add=True,
    )

    viewed = models.BooleanField(
        default=False
    )

    readed = models.BooleanField(
        default=False,
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.from_user}-{self.to_user}-{self.pk}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"From: {self.from_user} -- TO: {self.to_user}"
