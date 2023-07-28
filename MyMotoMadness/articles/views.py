from django.views import generic as views

from MyMotoMadness.articles.models import ArticlesModel


# Create your views here.
class CommonArticlesView(views.ListView):
    template_name = 'articles/articles_common.html'
    model = ArticlesModel


class ArticleCreateView(views.CreateView):
    ...


class ArticleUpdateView(views.UpdateView):
    ...


class ArticleDeleteView(views.DeleteView):
    ...
