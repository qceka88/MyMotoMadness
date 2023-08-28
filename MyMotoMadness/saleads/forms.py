from django import forms
from django.core import exceptions
from multiupload.fields import MultiMediaField

from MyMotoMadness.saleads.mixins import BikeTypeChoices
from MyMotoMadness.saleads.models import Motorcycles, MotoParts, MotoEquipmentGear, MotorcycleImages, \
    MotoEquipmentImages, MotoPartsImages


class Limits:
    MIN_FILES = 2
    MAX_FILES = 8
    MAX_FILE_SIZE = 1024 * 1024 * 5


class BaseMotorcycleForm(forms.ModelForm):
    class Meta:
        model = Motorcycles
        exclude = ('motorcycle_images',)
        widgets = {
            'owner': forms.HiddenInput(
            ),
            'bike_type': forms.Select(
                attrs={
                    'placeholder': 'Enter Motorcycle Model',
                    'style': "height: 35px",
                }
            ),
            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Motorcycle Brand',
                    'style': "height: 35px",
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Motorcycle Model',
                    'style': "height: 35px",
                }
            ),
            'engine_volume': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Engine Volume',
                    'style': "height: 35px",
                }
            ),
            'manufacture_year': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Manufacture Year',
                    'style': "height: 35px",
                }
            ),
            'odo_meter': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Odo Meter Data',
                    'style': "height: 35px",
                }
            ),
            'horse_power': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Horse Power',
                    'style': "height: 35px",
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter addition information about Motorcycle!'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Enter City',
                    'style': "height: 35px",
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Price for Motorcycle',
                    'style': "height: 35px",
                }
            ),
        }

    def save(self, commit=True):
        motorcycle = super(BaseMotorcycleForm, self).save(commit)
        for image_file in self.cleaned_data['motorcycle_images']:
            MotorcycleImages.objects.create(image=image_file, sale_ad=motorcycle)

        return motorcycle


class CreateMotorcycleForm(Limits, BaseMotorcycleForm):
    motorcycle_images = MultiMediaField(min_num=Limits.MIN_FILES,
                                        max_num=Limits.MAX_FILES,
                                        max_file_size=Limits.MAX_FILE_SIZE,
                                        media_type='image',
                                        label='Add Images:',
                                        )


class EditMotorcycleForm(Limits, BaseMotorcycleForm):
    BaseMotorcycleForm.Meta.exclude = ('motorcycle_images', 'owner')

    motorcycle_images = MultiMediaField(min_num=0,
                                        max_num=Limits.MAX_FILES,
                                        max_file_size=Limits.MAX_FILE_SIZE,
                                        media_type='image',
                                        label='Add Images:',
                                        required=False, )

    def clean(self):
        existing_bike_images = len(self.instance.motorcycleimages_set.all())
        images_for_add = len(self.cleaned_data['motorcycle_images'])

        try:
            images_for_delete = dict(self.data)['selected_images']
        except KeyError:
            images_for_delete = ''

        total = existing_bike_images - len(images_for_delete) + images_for_add
        if total < Limits.MIN_FILES:
            raise exceptions.ValidationError(
                {
                    "motorcycle_images": f'Minimum images for sale offer is {self.MIN_FILES} !'}
            )

        elif Limits.MAX_FILES < total:
            raise exceptions.ValidationError(
                {
                    "motorcycle_images": f'Maximum images for sale offer is {self.MAX_FILES}!'}
            )

        MotorcycleImages.objects.filter(id__in=images_for_delete).delete()
        return self.cleaned_data


class SearchMotorcycle(forms.Form):
    brand = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by brand.'
            }
        )
    )
    model = forms.CharField(
        required=False,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search by brand.'
            }
        )
    )
    bike_type = forms.ChoiceField(
        required=False,
        choices=BikeTypeChoices.choices()
    )


class BaseEquipmentGearForm(forms.ModelForm):
    class Meta:
        model = MotoEquipmentGear
        exclude = ('equipment_images',)
        widgets = {
            'owner': forms.HiddenInput(),
            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Equipment Brand'
                }
            ),
            'gear_type': forms.Select(
                attrs={
                    'placeholder': 'Select Equipment Model',
                    'style': "height: 35px",
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Equipment Model'
                }
            ),
            'material_type': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Material Type'
                }
            ),
            'manufacture_year': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Manufacture Year'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter addition information about Equipment Gear'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Enter City'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Price for Equipment'
                }
            ),
        }

    def save(self, commit=True):
        equipment = super(BaseEquipmentGearForm, self).save(commit)
        for image_file in self.cleaned_data['equipment_images']:
            MotoEquipmentImages.objects.create(image=image_file, sale_ad=equipment)

        return equipment


class CreateEquipmentGearForm(Limits, BaseEquipmentGearForm):
    equipment_images = MultiMediaField(min_num=Limits.MIN_FILES,
                                       max_num=Limits.MAX_FILES,
                                       max_file_size=Limits.MAX_FILE_SIZE,
                                       media_type='image',
                                       label='Add Images:',
                                       )


class EditEquipmentGearForm(Limits, BaseEquipmentGearForm):
    BaseEquipmentGearForm.Meta.exclude = ('equipment_images', 'owner')
    equipment_images = MultiMediaField(min_num=0,
                                       max_num=Limits.MAX_FILES,
                                       max_file_size=Limits.MAX_FILE_SIZE,
                                       media_type='image',
                                       label='Add Images:',
                                       required=False, )

    def clean(self):
        existing_equipment_images = len(self.instance.motoequipmentimages_set.all())
        images_for_add = len(self.cleaned_data['equipment_images'])

        try:
            images_for_delete = dict(self.data)['selected_images']
        except KeyError:
            images_for_delete = ''

        total = existing_equipment_images - len(images_for_delete) + images_for_add
        if total < Limits.MIN_FILES:
            raise exceptions.ValidationError(
                {
                    "equipment_images": f'Minimum images for sale offer is {self.MIN_FILES} !'}
            )

        elif Limits.MAX_FILES < total:
            raise exceptions.ValidationError(
                {
                    "equipment_images": f'Maximum images for sale offer is {self.MAX_FILES}!'}
            )

        MotoEquipmentImages.objects.filter(id__in=images_for_delete).delete()
        return self.cleaned_data


class BasePartsForm(forms.ModelForm):
    class Meta:
        model = MotoParts
        exclude = ('moto_part_images',)
        widgets = {
            'owner': forms.HiddenInput(),
            'type_of_part': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Type of Part'
                }
            ),
            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Brand of Part'
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Model of Part'
                }
            ),
            'for_bike': forms.TextInput(
                attrs={
                    'placeholder': 'Enter For What Bike is Part'
                }
            ),
            'manufacture_year': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Manufacture Year'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter addition information about bike Part'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Enter City'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Price for Part'
                }
            ),
        }

    def save(self, commit=True):
        parts = super(BasePartsForm, self).save(commit)
        for image_file in self.cleaned_data['moto_part_images']:
            MotoPartsImages.objects.create(image=image_file, sale_ad=parts)

        return parts


class CreatePartsForm(Limits, BasePartsForm):
    moto_part_images = MultiMediaField(min_num=Limits.MIN_FILES,
                                       max_num=Limits.MAX_FILES,
                                       max_file_size=Limits.MAX_FILE_SIZE,
                                       media_type='image',
                                       label='Add Images',
                                       )


class EditPartsForm(Limits, BasePartsForm):
    BasePartsForm.Meta.exclude = ('moto_part_images', 'owner')
    moto_part_images = MultiMediaField(min_num=0,
                                       max_num=Limits.MAX_FILES,
                                       max_file_size=Limits.MAX_FILE_SIZE,
                                       media_type='image',
                                       label='Add Images',
                                       required=False
                                       )

    def clean(self):
        existing_part_images = len(self.instance.motopartsimages_set.all())
        images_for_add = len(self.cleaned_data['moto_part_images'])

        try:
            images_for_delete = dict(self.data)['selected_images']
        except KeyError:
            images_for_delete = ''

        total = existing_part_images - len(images_for_delete) + images_for_add
        if total < Limits.MIN_FILES:
            raise exceptions.ValidationError(
                {
                    "moto_part_images": f'Minimum images for sale offer is {self.MIN_FILES} !'}
            )

        elif Limits.MAX_FILES < total:
            raise exceptions.ValidationError(
                {
                    "moto_part_images": f'Maximum images for sale offer is {self.MAX_FILES}!'}
            )

        MotoPartsImages.objects.filter(id__in=images_for_delete).delete()
        return self.cleaned_data
