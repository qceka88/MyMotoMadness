from django.urls import path

from MyMotoMadness.articles.views import CommonArticlesView

urlpatterns = [
    path('', CommonArticlesView.as_view(), name='common articles views'),

]