# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.saleads.froms import CreateMotorcycleForm, EditMotorcycleForm, DeleteMotorcycleForm, \
    CreateEquipmentGearForm
from MyMotoMadness.saleads.models import MotorcyclesModel, MotorcycleImages, MotoEquipmentGear, MotoEquipmentImages


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'


class MotorcyclesListViews(views.ListView):
    # template_name = 'sales/motorcycles'
    template_name = 'test_template/list_test.html'
    model = MotorcyclesModel


class MotorcyclesAddView(views.CreateView):
    # template_name = 'sales/motorcycles'
    template_name = 'test_template/create_test.html'
    model = MotorcyclesModel
    form_class = CreateMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')

    def form_valid(self, form):
        data = super().form_valid(form)
        moto = MotorcyclesModel.objects.all().last()
        for field in self.request.FILES.keys():
            for image_file in self.request.FILES.getlist(field):
                image = MotorcycleImages(images=image_file, motorcycle=moto)
                image.save()

            return data


class MotorcyclesEditView(views.UpdateView):
    # TODO: check for removing images
    # template_name = 'sales/motorcycles'
    template_name = 'test_template/edit_test.html'
    model = MotorcyclesModel
    form_class = EditMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class MotorcyclesDetailsView(views.DetailView):
    # template_name = 'sales/motorcycles'
    template_name = 'test_template/detail_test.html'
    model = MotorcyclesModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: Check is this proper bike connection
        bike = MotorcyclesModel.objects.filter(pk=context['object'].pk).get()
        context['pictures'] = bike.motorcycleimages_set.all()
        return context


class MotorcyclesDeleteView(views.DeleteView):
    # template_name = 'sales/motorcycles'
    template_name = 'test_template/delete_test.html'
    model = MotorcyclesModel
    form_class = DeleteMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class EquipmentGearListView(views.ListView):
    ...


class EquipmentGearAddView(views.CreateView):
    # template_name = 'sales/EquipemtnGear'
    template_name = 'test_template/create_test.html'
    model = MotoEquipmentGear
    form_class = CreateEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')

    def form_valid(self, form):
        data = super().form_valid(form)
        moto = MotorcyclesModel.objects.all().last()
        for field in self.request.FILES.keys():
            for image_file in self.request.FILES.getlist(field):
                image = MotoEquipmentImages(images=image_file, motorcycle=moto)
                image.save()

            return data


class EquipmentGearEditView(views.UpdateView):
    ...


class EquipmentGearDetailsView(views.DetailView):
    ...


class EquipmentGearDeleteView(views.DeleteView):
    ...
