from django.urls import path

from MyMotoMadness.articles.views import ArticlesView

urlpatterns = [
    path('', ArticlesView.as_view(), name='articles views'),
]