from django import forms

from MyMotoMadness.saleads.models import Motorcycles, MotoParts, MotoEquipmentGear


class BaseMotorcycleForm(forms.ModelForm):
    class Meta:
        model = Motorcycles
        fields = '__all__'

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
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Price for Motorcycle'
                }
            ),

        }


class CreateMotorcycleForm(BaseMotorcycleForm):
    ...


class EditMotorcycleForm(BaseMotorcycleForm):
    ...


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
