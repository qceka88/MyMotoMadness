from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.articles.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm
from MyMotoMadness.articles.models import ArticlesModel


# Create your views here.
class CommonArticlesView(views.ListView):
    template_name = 'articles/articles_common.html'
    model = ArticlesModel


class NewsListView(views.ListView):
    template_name = 'articles/articles_list.html'
    model = ArticlesModel

    def get_queryset(self):
        data = super().get_queryset().filter(article_type='News')
        return data


class AdvicesListView(views.ListView):
    template_name = 'articles/articles_list.html'
    model = ArticlesModel

    def get_queryset(self):
        data = super().get_queryset().filter(article_type='Advices')
        return data

class ArticleCreateView(views.CreateView):
    template_name = 'articles/create_article.html'
    model = ArticlesModel
    form_class = CreateArticleForm
    success_url = reverse_lazy('common articles views')

    def form_valid(self, form):
        data = super().form_valid(form)
        self.object.author = self.request.user
        self.object.save()
        return data


class ArticleDetailView(views.DetailView):
    template_name = 'articles/detail_article.html'
    model = ArticlesModel


class ArticleUpdateView(views.UpdateView):
    template_name = 'articles/edit_article.html'
    model = ArticlesModel
    form_class = EditArticleForm
    success_url = reverse_lazy('common articles views')


class ArticleDeleteView(views.DeleteView):
    template_name = 'articles/delete_article.html'
    model = ArticlesModel
    form_class = DeleteArticleForm
    success_url = reverse_lazy('common articles views')
