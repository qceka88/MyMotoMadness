from django.db import models


# ARTICLES MODELS
class ArticlesModel(models.Model):
    CHOICE_MENU = (('News', 'News'),
                   ('Advices', 'Advices'),
                   )

    title = models.CharField(
        max_length=30,
    )
    sub_title = models.CharField(
        max_length=30,
    )

    article_image = models.ImageField(
        upload_to='article_photos',
        blank=True,
        null=True,
    )

    description = models.TextField(

    )
    published = models.DateTimeField(
        auto_now_add=True,
    )
    author = models.CharField(
        max_length=30
    )
    article_type = models.CharField(
        max_length=30,
        choices=CHOICE_MENU,
    )

    def __str__(self):
        return f'{self.title}-{self.pk}'
