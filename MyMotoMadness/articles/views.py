from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.articles.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm
from MyMotoMadness.articles.mixins import CheckUserPermission
from MyMotoMadness.articles.models import ArticlesModel


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


class ArticleCreateView(CheckUserPermission, auth_mixins.PermissionRequiredMixin, views.CreateView):
    template_name = 'articles/create_article.html'
    model = ArticlesModel
    form_class = CreateArticleForm
    success_url = reverse_lazy('common articles views')
    permission_required = ['is_staff', 'is_superuser']

    def form_valid(self, form):
        data = super().form_valid(form)
        self.object.author = self.request.user
        self.object.save()
        return data


class ArticleDetailView(views.DetailView):
    template_name = 'articles/detail_article.html'
    model = ArticlesModel


class ArticleUpdateView(CheckUserPermission, views.UpdateView):
    template_name = 'articles/edit_article.html'
    model = ArticlesModel
    form_class = EditArticleForm
    success_url = reverse_lazy('common articles views')


class ArticleDeleteView(CheckUserPermission, views.DeleteView):
    template_name = 'articles/delete_article.html'
    model = ArticlesModel
    form_class = DeleteArticleForm
    success_url = reverse_lazy('common articles views')
