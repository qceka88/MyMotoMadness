# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.saleads.froms import CreateMotorcycleForm, EditMotorcycleForm, DeleteMotorcycleForm
from MyMotoMadness.saleads.models import MotorcyclesModel


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'


class MotorcyclesListViews(views.ListView):
    template_name = 'sales/motorcycles'
    model = MotorcyclesModel


class MotorcyclesAddView(views.CreateView):
    template_name = 'sales/motorcycles'
    model = MotorcyclesModel
    form_class = CreateMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class MotorcyclesEditView(views.UpdateView):
    template_name = 'sales/motorcycles'
    model = MotorcyclesModel
    form_class = EditMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class MotorcyclesDetailsView(views.DetailView):
    template_name = 'sales/motorcycles'
    model = MotorcyclesModel


class MotorcyclesDeleteView(views.DeleteView):
    template_name = 'sales/motorcycles'
    model = MotorcyclesModel
    form_class = DeleteMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')

#TODO : impelement the logic
class EquipmentGearListView(views.ListView):
    ...


class EquipmentGearAddView(views.ListView):
    ...


class EquipmentGearEditView(views.UpdateView):
    ...


class EquipmentGearDetailsView(views.DetailView):
    ...


class EquipmentGearDeleteView(views.DeleteView):
    ...
