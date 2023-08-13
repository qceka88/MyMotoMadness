"""

MAIN URLS

"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('sales/', include('MyMotoMadness.saleads.urls')),
                  path('articles/', include('MyMotoMadness.articles.urls')),
                  path('accounts/', include('MyMotoMadness.accounts.urls')),
                  path('', include('MyMotoMadness.common.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
