"""
MAIN URLS

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include('MyMotoMadness.saleads.urls')),
    path('articles/', include('MyMotoMadness.articles.urls')),
    path('accounts/', include('MyMotoMadness.accounts.urls')),
    path('', include('MyMotoMadness.common.urls')),
]

# message buttons
#<i class='far fa-message'></i>
#<i class='fas fa-message'></i>