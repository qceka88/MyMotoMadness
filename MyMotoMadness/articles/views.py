from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.articles.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm
from MyMotoMadness.articles.models import ArticlesModel


# Create your views here.
class CommonArticlesView(views.ListView):
    template_name = 'articles/articles_common.html'
    model = ArticlesModel


class ArticleCreateView(views.CreateView):
    template_name = 'articles'
    model = ArticlesModel
    form_class = CreateArticleForm
    success_url = reverse_lazy('common articles views')


class ArticleDetailView(views.DetailView):
    template_name = 'articles'
    model = ArticlesModel


class ArticleUpdateView(views.UpdateView):
    template_name = 'articles'
    model = ArticlesModel
    form_class = EditArticleForm
    success_url = reverse_lazy('common articles views')


class ArticleDeleteView(views.DeleteView):
    template_name = 'articles'
    model = ArticlesModel
    form_class = DeleteArticleForm
    success_url = reverse_lazy('common articles views')

