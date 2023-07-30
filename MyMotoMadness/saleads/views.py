# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.saleads.froms import CreateMotorcycleForm, EditMotorcycleForm, DeleteMotorcycleForm, \
    CreateEquipmentGearForm, EditEquipmentGearForm, DeleteEquipmentGearForm, CreatePartsForm,EditPartsForm,DeletePartsForm
from MyMotoMadness.saleads.models import MotorcyclesModel, MotorcycleImages, MotoEquipmentGear, MotoEquipmentImages


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'


class MotorcyclesListViews(views.ListView):
    template_name = 'sales/motorcycles'
    #template_name = 'test_template/list_test.html'
    model = MotorcyclesModel


class MotorcyclesAddView(views.CreateView):
    template_name = 'sales/motorcycles'
    #template_name = 'test_template/create_test.html'
    model = MotorcyclesModel
    form_class = CreateMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')

    def form_valid(self, form):
        data = super().form_valid(form)
        moto = MotorcyclesModel.objects.all().last()
        for field in self.request.FILES.keys():
            for image_file in self.request.FILES.getlist(field):
                image = MotorcycleImages(image=image_file, motorcycle=moto)
                image.save()

            return data


class MotorcyclesEditView(views.UpdateView):
    # TODO: check for removing or replace multiple images in edit view
    template_name = 'sales/motorcycles'
    #template_name = 'test_template/edit_test.html'
    model = MotorcyclesModel
    form_class = EditMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class MotorcyclesDetailsView(views.DetailView):
    template_name = 'sales/motorcycles'
    #template_name = 'test_template/detail_test.html'
    model = MotorcyclesModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # TODO: when user model is created change with  request.user.motorcyclesmodel.objects.filter
        bike = MotorcyclesModel.objects.filter(pk=context['object'].pk).get()
        context['bike_pictures'] = bike.motorcycleimages_set.all()
        return context


class MotorcyclesDeleteView(views.DeleteView):
    # template_name = 'sales/motorcycles'
    template_name = 'test_template/delete_test.html'
    model = MotorcyclesModel
    form_class = DeleteMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class EquipmentGearListView(views.ListView):
    template_name = 'test_template/list_test.html'
    model = MotoEquipmentGear


class EquipmentGearAddView(views.CreateView):
    # template_name = 'sales/equipment_gear/'
    template_name = 'test_template/create_test.html'
    model = MotoEquipmentGear
    form_class = CreateEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')

    def form_valid(self, form):
        data = super().form_valid(form)
        # TODO: when user model is created change with  request.user.motorcycleequipmentgear.objects.all
        equipment = MotoEquipmentGear.objects.all().last()
        for field in self.request.FILES.keys():
            for image_file in self.request.FILES.getlist(field):
                image = MotoEquipmentImages(image=image_file, moto_equipment=equipment)
                image.save()

            return data


class EquipmentGearEditView(views.UpdateView):
    # template_name = 'sales/equipment_gear/'
    template_name = 'test_template/edit_test.html'
    model = MotoEquipmentGear
    form_class = EditEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')


class EquipmentGearDetailsView(views.DetailView):
    template_name = 'test_template/detail_test.html'
    model = MotoEquipmentGear

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        equipment_gear = MotoEquipmentGear.objects.filter(pk=data['object'].pk).get()
        data['equipment_pictures'] = equipment_gear.motoequipmentimages_set.all()
        return data


class EquipmentGearDeleteView(views.DeleteView):
    # template_name = 'sales/equipment_gear/'
    template_name = 'test_template/delete_test.html'
    model = MotoEquipmentGear
    form_class = DeleteEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')
