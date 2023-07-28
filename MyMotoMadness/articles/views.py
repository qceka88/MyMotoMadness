from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.articles.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm
from MyMotoMadness.articles.models import ArticlesModel


# Create your views here.
class CommonArticlesView(views.ListView):
    # template_name = 'articles/articles_common.html'
    template_name = 'test_template/list_test.html'
    model = ArticlesModel


class ArticleCreateView(views.CreateView):
    template_name = 'test_template/create_test.html'
    model = ArticlesModel
    form_class = CreateArticleForm
    success_url = reverse_lazy('common articles views')


class ArticleDetailView(views.DetailView):
    template_name = 'test_template/detail_test.html'
    model = ArticlesModel


class ArticleUpdateView(views.UpdateView):
    template_name = 'test_template/edit_test.html'
    model = ArticlesModel
    form_class = EditArticleForm
    success_url = reverse_lazy('common articles views')


class ArticleDeleteView(views.DeleteView):
    template_name = 'test_template/delete_test.html'
    model = ArticlesModel
    form_class = DeleteArticleForm
    success_url = reverse_lazy('common articles views')

