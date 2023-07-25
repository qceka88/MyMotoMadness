from django.db import models


# ARTICLES MODELS
class ArticlesModel(models.Model):
    title = models.CharField(
        max_length=30,
    )
    sub_title = models.CharField(
        max_length=30,
    )

    description = models.TextField(

    )
    published = models.DateTimeField(
        auto_created=True,
    )
    author = models.CharField(
        max_length=30
    )
    article_type = models.CharField(
        max_length=30,
        #news or useful information
    )
