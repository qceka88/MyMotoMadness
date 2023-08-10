from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.saleads.forms import CreateMotorcycleForm, EditMotorcycleForm, \
    CreateEquipmentGearForm, EditEquipmentGearForm, CreatePartsForm, EditPartsForm
from MyMotoMadness.saleads.mixins import AddPicturesToSaleOffer, CheckForRestrictionAds
from MyMotoMadness.saleads.models import Motorcycles, MotorcycleImages, MotoEquipmentGear, MotoEquipmentImages, \
    MotoParts, MotoPartsImages


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sale_offers'] = []
        for queryset_offers in (
                Motorcycles.objects.all(),
                MotoEquipmentGear.objects.all(),
                MotoParts.objects.all()
        ):
            context['sale_offers'].extend(queryset_offers)

        return context


class MotorcyclesListViews(views.ListView):
    template_name = 'sales/motorcycles/list_motorcycles.html'
    model = Motorcycles


class MotorcyclesAddView(auth_mixins.LoginRequiredMixin, AddPicturesToSaleOffer, views.CreateView):
    template_name = 'sales/motorcycles/create_motorcycle.html'
    model = Motorcycles
    form_class = CreateMotorcycleForm
    success_url = reverse_lazy('list motorcycle view')

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            self.object.owner = self.request.user
            self.object.save()
            return data

        return self.form_invalid(form)


class MotorcyclesEditView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, AddPicturesToSaleOffer,
                          views.UpdateView):
    template_name = 'sales/motorcycles/edit_motorcycle.html'
    model = Motorcycles
    form_class = EditMotorcycleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bike_pictures'] = context['object'].motorcycleimages_set.all()
        return context

    def post(self, request, *args, **kwargs):
        #selected_images = request.POST.getlist('selected_images')
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            return data

        return data

    def get_success_url(self):
        return reverse_lazy('detail motorcycle view', kwargs={'pk': self.object.pk})


class MotorcyclesDetailsView(views.DetailView):
    template_name = 'sales/motorcycles/details_motorcycle.html'
    model = Motorcycles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bike_pictures'] = context['object'].motorcycleimages_set.all()
        return context


class MotorcyclesDeleteView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, views.DeleteView):
    template_name = 'sales/motorcycles/delete_motorcycle.html'
    model = Motorcycles
    success_url = reverse_lazy('list motorcycle view')


class EquipmentGearListView(views.ListView):
    template_name = 'sales/equipment_gear/equipment_list.html'
    model = MotoEquipmentGear


class EquipmentGearAddView(auth_mixins.LoginRequiredMixin, AddPicturesToSaleOffer, views.CreateView):
    template_name = 'sales/equipment_gear/add_equipment.html'
    model = MotoEquipmentGear
    form_class = CreateEquipmentGearForm
    success_url = reverse_lazy('list equipment gear view')

    def form_valid(self, form):
        data = super().form_valid(form)
        self.add_pictures_to_sale_offer(self.object, self.request, self.request.user, MotoEquipmentImages)
        return data


class EquipmentGearEditView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, AddPicturesToSaleOffer,
                            views.UpdateView):
    template_name = 'sales/equipment_gear/edit_equipment.html'
    model = MotoEquipmentGear
    form_class = EditEquipmentGearForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipment_pictures'] = context['object'].motoequipmentimages_set.all()
        return context

    def form_valid(self, form):
        data = super().form_valid(form)
        self.add_pictures_to_sale_offer(self.object, self.request, self.request.user, MotoEquipmentImages)
        return data

    def post(self, request, *args, **kwargs):
        selected_images = request.POST.getlist('selected_images')
        MotoEquipmentImages.objects.filter(id__in=selected_images).delete()
        data = super().post(request, *args, **kwargs)
        return data

    def get_success_url(self):
        return reverse_lazy('detail equipment gear view', kwargs={'pk': self.object.pk})


class EquipmentGearDetailsView(views.DetailView):
    template_name = 'sales/equipment_gear/details_equipment.html'
    model = MotoEquipmentGear

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipment_pictures'] = context['object'].motoequipmentimages_set.all()
        return context


class EquipmentGearDeleteView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, views.DeleteView):
    template_name = 'sales/equipment_gear/delete_equipment.html'
    model = MotoEquipmentGear
    success_url = reverse_lazy('list equipment gear view')


class PartsListView(views.ListView):
    template_name = 'sales/moto_parts/list_parts.html'
    model = MotoParts


class PartsAddView(auth_mixins.LoginRequiredMixin, AddPicturesToSaleOffer, views.CreateView):
    template_name = 'sales/moto_parts/add_part.html'
    model = MotoParts
    form_class = CreatePartsForm
    success_url = reverse_lazy('list bike parts view')

    def form_valid(self, form):
        data = super().form_valid(form)
        self.add_pictures_to_sale_offer(self.object, self.request, self.request.user, MotoPartsImages)
        return data


class PartsEditView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, AddPicturesToSaleOffer,
                    views.UpdateView):
    template_name = 'sales/moto_parts/edit_part.html'
    model = MotoParts
    form_class = EditPartsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_pictures'] = context['object'].motopartsimages_set.all()
        return context

    def form_valid(self, form):
        data = super().form_valid(form)
        self.add_pictures_to_sale_offer(self.object, self.request, self.request.user, MotoPartsImages)
        return data

    def post(self, request, *args, **kwargs):
        selected_images = request.POST.getlist('selected_images')
        MotoPartsImages.objects.filter(id__in=selected_images).delete()
        data = super().post(request, *args, **kwargs)
        return data

    def get_success_url(self):
        return reverse_lazy('detail bike parts view', kwargs={'pk': self.object.pk})


class PartsDetailsView(views.DetailView):
    template_name = 'sales/moto_parts/details_parts.html'
    model = MotoParts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_pictures'] = context['object'].motopartsimages_set.all()
        return context


class PartsDeleteView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, views.DeleteView):
    template_name = 'sales/moto_parts/delete_parts.html'
    model = MotoParts
    success_url = reverse_lazy('list bike parts view')
