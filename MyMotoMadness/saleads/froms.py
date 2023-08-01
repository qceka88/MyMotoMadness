from django import forms

from MyMotoMadness.saleads.models import MotorcyclesModel, MotoParts, MotoEquipmentGear


class BaseMotorcycleForm(forms.ModelForm):
    class Meta:
        model = MotorcyclesModel
        fields = '__all__'

        widgets = {
            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Motorcycle Brand'
                }
            ),
            'model': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Motorcycle Brand'
                }
            ),
            'engine_volume': forms.TextInput(
                attrs={
                    'placeholder': 'Enter Engine Volume'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter addition information about Motorcycle!'
                }
            ),
            'owner': forms.HiddenInput(),
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
        }

        # TODO: Add placeholders


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
        }

        # TODO: Add placeholders


class CreatePartsForm(BasePartsForm):
    ...


class EditPartsForm(BasePartsForm):
    ...
