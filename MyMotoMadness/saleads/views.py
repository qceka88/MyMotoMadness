from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views

from MyMotoMadness.saleads.forms import CreateMotorcycleForm, EditMotorcycleForm, \
    CreateEquipmentGearForm, EditEquipmentGearForm, CreatePartsForm, EditPartsForm, SearchMotorcycle, SearchEquipment, \
    SearchPart
from MyMotoMadness.saleads.mixins import CheckForRestrictionAds, CheckAdminStaffPermission, NotApprovedContent, \
    GetQuerySetListViewsMixin
from MyMotoMadness.saleads.models import Motorcycles, MotoEquipmentGear, MotoParts


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sale_offers'] = []
        for queryset_offers in (
                Motorcycles.objects.all().order_by('-published')[:5],
                MotoEquipmentGear.objects.all().order_by('-published')[:5],
                MotoParts.objects.all().order_by('-published')[:5]
        ):
            context['sale_offers'].extend(queryset_offers)

        return context


class NotApprovedOffersView(CheckAdminStaffPermission, views.ListView):
    template_name = 'sales/not_approved_offers.html'
    paginate_by = 8

    def get_queryset(self):
        queryset = (list(Motorcycles.objects.filter(approved=False)) +
                    list(MotoEquipmentGear.objects.filter(approved=False)) +
                    list(MotoParts.objects.filter(approved=False)))

        return queryset


class MotorcyclesListViews(GetQuerySetListViewsMixin, views.ListView):
    template_name = 'sales/motorcycles/list_motorcycles.html'
    model = Motorcycles
    paginate_by = 8

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        data['search_motorcycles'] = SearchMotorcycle(self.request.GET)
        return data


class MotorcyclesAddView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'sales/motorcycles/create_motorcycle.html'
    model = Motorcycles
    form_class = CreateMotorcycleForm

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            self.object.owner = self.request.user
            self.object.save()
            return data

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('detail motorcycle view', kwargs={'pk': self.object.pk})


class MotorcyclesEditView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, views.UpdateView):
    template_name = 'sales/motorcycles/edit_motorcycle.html'
    model = Motorcycles
    form_class = EditMotorcycleForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bike_pictures'] = context['object'].motorcycleimages_set.all()
        return context

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            if not self.request.user.is_staff and not self.request.user.is_superuser:
                self.object.approved = False
                self.object.save()
            return data

        return data

    def get_success_url(self):
        return reverse_lazy('detail motorcycle view', kwargs={'pk': self.object.pk})


class MotorcyclesDetailsView(NotApprovedContent, views.DetailView):
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


class EquipmentGearListView(GetQuerySetListViewsMixin, views.ListView):
    template_name = 'sales/equipment_gear/equipment_list.html'
    model = MotoEquipmentGear
    paginate_by = 8

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['search_equipment'] = SearchEquipment(self.request.GET)
        return data


class EquipmentGearAddView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'sales/equipment_gear/add_equipment.html'
    model = MotoEquipmentGear
    form_class = CreateEquipmentGearForm

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            self.object.owner = self.request.user
            self.object.save()
            return data

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('detail equipment gear view', kwargs={'pk': self.object.pk})

class EquipmentGearEditView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, views.UpdateView):
    template_name = 'sales/equipment_gear/edit_equipment.html'
    model = MotoEquipmentGear
    form_class = EditEquipmentGearForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['equipment_pictures'] = context['object'].motoequipmentimages_set.all()
        return context

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            if not self.request.user.is_staff and not self.request.user.is_superuser:
                self.object.approved = False
                self.object.save()
            return data

        return data

    def get_success_url(self):
        return reverse_lazy('detail equipment gear view', kwargs={'pk': self.object.pk})


class EquipmentGearDetailsView(NotApprovedContent, views.DetailView):
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


class PartsListView(GetQuerySetListViewsMixin, views.ListView):
    template_name = 'sales/moto_parts/list_parts.html'
    model = MotoParts
    paginate_by = 8

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['search_part'] = SearchPart(self.request.GET)
        return data


class PartsAddView(auth_mixins.LoginRequiredMixin, views.CreateView):
    template_name = 'sales/moto_parts/add_part.html'
    model = MotoParts
    form_class = CreatePartsForm

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            self.object.owner = self.request.user
            self.object.save()
            return data

        return self.form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('detail bike parts view', kwargs={'pk': self.object.pk})

class PartsEditView(auth_mixins.LoginRequiredMixin, CheckForRestrictionAds, views.UpdateView):
    template_name = 'sales/moto_parts/edit_part.html'
    model = MotoParts
    form_class = EditPartsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['part_pictures'] = context['object'].motopartsimages_set.all()
        return context

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        form = self.get_form()

        if form.is_valid():
            if not self.request.user.is_staff and not self.request.user.is_superuser:
                self.object.approved = False
                self.object.save()
            return data

        return data

    def get_success_url(self):
        return reverse_lazy('detail bike parts view', kwargs={'pk': self.object.pk})


class PartsDetailsView(NotApprovedContent, views.DetailView):
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
