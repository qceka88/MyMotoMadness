from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.saleads.froms import CreateMotorcycleForm, EditMotorcycleForm, DeleteMotorcycleForm, \
    CreateEquipmentGearForm, EditEquipmentGearForm, DeleteEquipmentGearForm, CreatePartsForm, EditPartsForm
from MyMotoMadness.saleads.models import MotorcyclesModel, MotorcycleImages, MotoEquipmentGear, MotoEquipmentImages, \
    MotoParts, MotoPartsImages


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'


class MotorcyclesListViews(views.ListView):
    template_name = 'sales/motorcycles'
    # template_name = 'test_template/list_test.html'
    model = MotorcyclesModel


class MotorcyclesAddView(views.CreateView):
    template_name = 'sales/motorcycles'
    # template_name = 'test_template/create_test.html'
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
    # template_name = 'test_template/edit_test.html'
    model = MotorcyclesModel
    form_class = EditMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class MotorcyclesDetailsView(views.DetailView):
    template_name = 'sales/motorcycles'
    # template_name = 'test_template/detail_test.html'
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
    # TODO: Check form_class is needed
    form_class = DeleteMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')


class EquipmentGearListView(views.ListView):
    template_name = 'sales/equipment_gear/equipment_list.html'
    model = MotoEquipmentGear


class EquipmentGearAddView(views.CreateView):
    template_name = 'sales/equipment_gear/'
    # template_name = 'test_template/create_test.html'
    model = MotoEquipmentGear
    form_class = CreateEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')

    def form_valid(self, form):
        form.Meta.model.owner = self.request.user
        form.save()
        data = super().form_valid(form)
        for field in self.request.FILES.keys():
            for image_file in self.request.FILES.getlist(field):
                image = MotoEquipmentImages(image=image_file, sale_ad=self.object)
                image.save()

        return data


class EquipmentGearEditView(views.UpdateView):
    template_name = 'sales/equipment_gear/'
    # template_name = 'test_template/edit_test.html'
    model = MotoEquipmentGear
    form_class = EditEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')


class EquipmentGearDetailsView(views.DetailView):
    template_name = 'sales/equipment_gear/'
    # template_name = 'test_template/detail_test.html'
    model = MotoEquipmentGear

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        equipment_gear = MotoEquipmentGear.objects.filter(pk=data['object'].pk).get()
        data['equipment_pictures'] = equipment_gear.motoequipmentimages_set.all()
        return data


class EquipmentGearDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'sales/equipment_gear/'
    # template_name = 'test_template/delete_test.html'
    model = MotoEquipmentGear
    # TODO: Check form_class is needed
    form_class = DeleteEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')


class PartsListView(views.ListView):
    template_name = 'sales/moto_parts/list_parts.html'
    model = MotoParts


class PartsAddView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'sales/moto_parts/add_part.html'
    model = MotoParts
    form_class = CreatePartsForm
    success_url = reverse_lazy('list bike parts view')

    def form_valid(self, form):
        form.Meta.model.owner = self.request.user
        form.save()
        data = super().form_valid(form)
        for field in self.request.FILES.keys():
            for image_file in self.request.FILES.getlist(field):
                image = MotoPartsImages(image=image_file, sale_ad=self.object)
                image.save()
        return data


class PartsEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    template_name = 'sales/moto_parts/part_edit.html'
    model = MotoParts
    form_class = EditPartsForm
    success_url = reverse_lazy('list bike parts view')


class PartsDetailsView(views.DetailView):
    template_name = 'sales/moto_parts/details_parts.html'
    model = MotoParts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        part = MotoParts.objects.filter(pk=context['object'].pk).get()
        context['part_pictures'] = part.motopartsimages_set.all()
        return context


class PartsDeleteView(auth_mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'sales/moto_parts/delete_parts.html'
    model = MotoParts
    success_url = reverse_lazy('list bike parts view')
