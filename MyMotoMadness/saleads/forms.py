from django import forms
from django.core import exceptions
from multiupload.fields import MultiMediaField

from MyMotoMadness.saleads.models import Motorcycles, MotoParts, MotoEquipmentGear, MotorcycleImages


class Limits:
    MIN_FILES = 2
    MAX_FILES = 8
    MAX_FILE_SIZE = 1024 * 1024 * 5


class BaseMotorcycleForm(forms.ModelForm):
    class Meta:
        model = Motorcycles
        exclude = ('images', 'approved',)
        widgets = {
            'owner': forms.HiddenInput(

            ),
            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Motorcycle Brand'
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Motorcycle Model'
                }
            ),
            'engine_volume': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Engine Volume'
                }
            ),
            'manufacture_year': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Manufacture Year'
                }
            ),
            'horse_power': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter Horse Power'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter addition information about Motorcycle!'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Enter City'
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Price for Motorcycle'
                }
            ),
        }

    def save(self, commit=True):
        motorcycle = super(BaseMotorcycleForm, self).save(commit)
        for image_file in self.cleaned_data['images']:
            MotorcycleImages.objects.create(image=image_file, sale_ad=motorcycle)

        return motorcycle


class CreateMotorcycleForm(Limits, BaseMotorcycleForm):
    images = MultiMediaField(min_num=Limits.MIN_FILES,
                             max_num=Limits.MAX_FILES,
                             max_file_size=Limits.MAX_FILE_SIZE,
                             media_type='image'
                             )


class EditMotorcycleForm(Limits, BaseMotorcycleForm):
    images = MultiMediaField(min_num=0,
                             max_num=Limits.MAX_FILES,
                             max_file_size=Limits.MAX_FILE_SIZE,
                             media_type='image',
                             label='Add Images:',
                             required=False, )

    def clean(self):
        existing_bike_images = len(self.instance.motorcycleimages_set.all())
        print(f'curernt qty {existing_bike_images}')
        images_for_add = len(self.cleaned_data['images'])

        try:
            images_for_delete = dict(self.data)['selected_images']
        except KeyError:
            images_for_delete = ''

        total = existing_bike_images - len(images_for_delete) + images_for_add
        print(f"for delete{images_for_delete}")
        print(f"for add {images_for_add}")
        print(f"total {total}")
        if total < Limits.MIN_FILES:
            raise exceptions.ValidationError(
                {
                    "images": f'Minimum images for sale offer is {self.MIN_FILES} !'}
            )

        elif Limits.MAX_FILES < total:
            print(f'limit{Limits.MAX_FILES }')
            raise exceptions.ValidationError(
                {
                    "images": f'Maximum images for sale offer is {self.MAX_FILES}!'}
            )

        MotorcycleImages.objects.filter(id__in=images_for_delete).delete()
        return self.cleaned_data


class BaseEquipmentGearForm(forms.ModelForm):
    class Meta:
        model = MotoEquipmentGear
        fields = '__all__'
        widgets = {
            'owner': forms.HiddenInput(),
            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Equipment Brand'
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


class CreateEquipmentGearForm(BaseEquipmentGearForm):
    ...


class EditEquipmentGearForm(BaseEquipmentGearForm):
    ...


class BasePartsForm(forms.ModelForm):
    class Meta:
        model = MotoParts
        fields = '__all__'
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


class CreatePartsForm(BasePartsForm):
    ...


class EditPartsForm(BasePartsForm):
    ...
