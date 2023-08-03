from django.urls import path

from MyMotoMadness.articles.views import CommonArticlesView, ArticleCreateView, \
    ArticleUpdateView, ArticleDeleteView, ArticleDetailView, TestListView

urlpatterns = [
    path('', CommonArticlesView.as_view(), name='common articles views'),
    path('test-list/', TestListView.as_view(), name='test list articles views'),
    path('add/', ArticleCreateView.as_view(), name='add article view'),
    path('edit/<int:pk>/', ArticleUpdateView.as_view(), name='edit article view'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete article view'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail article view'),
]
