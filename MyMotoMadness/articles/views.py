from django.views import generic as views

from MyMotoMadness.articles.models import ArticlesModel


# Create your views here.
class ArticlesView(views.ListView):
    template_name = 'articles/articles_common.html'
    model = ArticlesModel
