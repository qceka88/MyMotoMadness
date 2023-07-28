from django.urls import path

from MyMotoMadness.saleads.views import CommonSaleView

# Sale ads URLS
urlpatterns = [
    path('', CommonSaleView.as_view(), name='common sale view'),
]
