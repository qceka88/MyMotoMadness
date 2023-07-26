from django.contrib import admin

from MyMotoMadness.articles.models import ArticlesModel


# Register your models here.
@admin.register(ArticlesModel)
class ArticleAdminForm(admin.ModelAdmin):
    ...
