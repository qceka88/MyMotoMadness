from django.urls import path, include

from MyMotoMadness.saleads.views import CommonSaleView, MotorcyclesListViews, MotorcyclesAddView, \
    MotorcyclesDetailsView, MotorcyclesEditView, MotorcyclesDeleteView, EquipmentGearListView, EquipmentGearAddView, \
    EquipmentGearEditView, EquipmentGearDetailsView, EquipmentGearDeleteView

# Sale offers URLS
urlpatterns = [
    path('', CommonSaleView.as_view(), name='common sale view'),
    path('motorcycles/', include([
        path('', MotorcyclesListViews.as_view(), name='list motorcycle view'),
        path('add/', MotorcyclesAddView.as_view(), name='add motorcycle view'),
        path('edit/<int:pk>/', MotorcyclesEditView.as_view(), name='edit motorcycle view'),
        path('detail/<int:pk>/', MotorcyclesDetailsView.as_view(), name='detail motorcycle view'),
        path('delete/<int:pk>/', MotorcyclesDeleteView.as_view(), name='delete motorcycle view'),
    ])),
    path('equipment-gear/', include([
        path('', EquipmentGearListView.as_view(), name='list equipment gear view'),
        path('add/', EquipmentGearAddView.as_view(), name='add equipment gear view'),
        path('edit/<int:pk>/', EquipmentGearEditView.as_view(), name='edit equipment gear view'),
        path('detail/<int:pk>/', EquipmentGearDetailsView.as_view(), name='detail equipment gear view'),
        path('delete/<int:pk>/', EquipmentGearDeleteView.as_view(), name='delete equipment gear view'),
    ]))
]
