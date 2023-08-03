from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ArticlesModel(models.Model):
    CHOICE_MENU = (
        ('News', 'News'),
        ('Advices', 'Advices'),
    )

    title = models.CharField(
        max_length=30,
    )
    sub_title = models.CharField(
        max_length=100,
    )

    article_image = models.ImageField(
        upload_to='photos/article_photos',
        blank=True,
        null=True,
    )

    description = models.TextField(

    )
    published = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    article_type = models.CharField(
        max_length=30,
        choices=CHOICE_MENU,
    )

    def __str__(self):
        return f'{self.title}-{self.pk}, {self.article_type}'
