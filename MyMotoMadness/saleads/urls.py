from django.urls import path, include

from MyMotoMadness.saleads.views import CommonSaleView, MotorcyclesListViews, MotorcyclesAddView, \
    MotorcyclesDetailsView, MotorcyclesEditView, MotorcyclesDeleteView

# Sale ads URLS
urlpatterns = [
    path('', CommonSaleView.as_view(), name='common sale view'),
    path('motorcycles/', include([
        path('', MotorcyclesListViews.as_view(), name='list motorcycle view'),
        path('add/', MotorcyclesAddView.as_view(), name='add motorcycle view'),
        path('edit/<int:pk>/', MotorcyclesEditView.as_view(), name='edit motorcycle view'),
        path('detail/<int:pk>/', MotorcyclesDetailsView.as_view(), name='detail motorcycle view'),
        path('delete/<int:pk>/', MotorcyclesDeleteView.as_view(), name='delete motorcycle view'),
    ])),
]
