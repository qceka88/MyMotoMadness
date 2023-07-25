from django.urls import path

from MyMotoMadness.common.views import IndexView

# COMMON URLS
urlpatterns = [
    path('', IndexView.as_view(), name='home-page')
]
