from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.articles.forms import CreateArticleForm, EditArticleForm, DeleteArticleForm, SearchArticleForm
from MyMotoMadness.articles.mixins import CheckUserArticlePermission
from MyMotoMadness.articles.models import ArticlesModel


class CommonArticlesView(views.TemplateView):
    template_name = 'articles/articles_common.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['advices_list'] = ArticlesModel.objects.filter(article_type='Advices').order_by('published')[:3]
        context['news_list'] = ArticlesModel.objects.filter(article_type='News').order_by('published')[:3]
        return context


class NewsListView(views.ListView):
    template_name = 'articles/news_list.html'
    model = ArticlesModel
    paginate_by = 8

    def get_queryset(self):
        queryset = ArticlesModel.objects.filter(article_type='News').order_by('-published')

        for field, value in self.request.GET.items():
            if value and field != 'page':
                queryset = queryset.filter(**{field: value})

        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['search_news'] = SearchArticleForm(self.request.GET)
        return data


class AdvicesListView(views.ListView):
    template_name = 'articles/advices_list.html'
    model = ArticlesModel
    paginate_by = 8

    def get_queryset(self):
        queryset = ArticlesModel.objects.filter(article_type='Advices')
        for field, value in self.request.GET.items():
            if value and field != 'page':
                queryset = queryset.filter(**{field: value})

        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['search_advices'] = SearchArticleForm(self.request.GET)
        return data


class ArticleCreateView(CheckUserArticlePermission, views.CreateView):
    template_name = 'articles/create_article.html'
    model = ArticlesModel
    form_class = CreateArticleForm

    def form_valid(self, form):
        data = super().form_valid(form)
        self.object.author = self.request.user
        self.object.save()
        return data

    def get_success_url(self):
        return reverse_lazy('detail article view', kwargs={'pk': self.object.pk})


class ArticleDetailView(views.DetailView):
    template_name = 'articles/detail_article.html'
    model = ArticlesModel


class ArticleUpdateView(CheckUserArticlePermission, views.UpdateView):
    template_name = 'articles/edit_article.html'
    model = ArticlesModel
    form_class = EditArticleForm
    success_url = reverse_lazy('common articles views')

    def get_success_url(self):
        return reverse_lazy('detail article view', kwargs={'pk': self.object.pk})


class ArticleDeleteView(CheckUserArticlePermission, views.DeleteView):
    template_name = 'articles/delete_article.html'
    model = ArticlesModel
    form_class = DeleteArticleForm
    success_url = reverse_lazy('common articles views')
