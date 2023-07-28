# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.saleads.froms import CreateMotorcycleForm, EditMotorcycleForm, DeleteMotorcycleForm
from MyMotoMadness.saleads.models import MotorcyclesModel


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'


class MotorcyclesListViews(views.ListView):
    template_name = 'test_template/list_test.html'
    model = MotorcyclesModel


class MotorcyclesAddView(views.CreateView):
    template_name = 'test_template/create_test.html'
    model = MotorcyclesModel
    form_class = CreateMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class MotorcyclesEditView(views.UpdateView):
    template_name = 'test_template/edit_test.html'
    model = MotorcyclesModel
    form_class = EditMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class MotorcyclesDetailsView(views.DetailView):
    template_name = 'test_template/detail_test.html'
    model = MotorcyclesModel


class MotorcyclesDeleteView(views.DeleteView):
    template_name = 'test_template/delete_test.html'
    model = MotorcyclesModel
    form_class = DeleteMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')
