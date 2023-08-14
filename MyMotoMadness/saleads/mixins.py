from enum import Enum

from django.shortcuts import redirect


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(c.value, c.value) for c in cls]


class BikeTypeChoices(ChoicesMixin, Enum):
    SUPERSPORT = 'SuperSport'
    SPORT = 'SportBike'
    CHOPPER = 'Chopper'
    BOBER = 'Bober'
    CAFE_RACER = 'Cafe Racer'
    ENDURO = 'Enduro'
    CROSS = 'Cross'
    CUSTOM = 'Custom Bike'
    CRUISER = 'Cruiser'
    NAKED = 'Naked Bike'
    STREET_FIGHTER = 'Street Fighter'
    SCOOTER = 'Scooter'
    RETRO = 'Retro Bike'
    OTHER = 'Other..'


class ProtectionGearTypeChoices(ChoicesMixin, Enum):
    HELMET = 'Helmet'
    RACE_SUIT_1PT = 'Race Suit One Part'
    RACE_SUIT_2PT = 'Race Suit Two Parts'
    BONNET = 'Bonnet'
    BOOTS = 'Boots'
    GLOVES = 'Gloves'
    PROTECTORS = 'Protectors'
    OTHER = 'Other..'


class CheckForRestrictionAds:

    def dispatch(self, request, *args, **kwargs):
        data = super().dispatch(request, *args, **kwargs)
        if request.user.pk != self.object.owner.pk and not request.user.is_superuser and not request.user.is_staff:
            return redirect('home-page')

        return data


class CheckAdminStaffPermission:

    def dispatch(self, request, *args, **kwargs):
        data = super().dispatch(request, *args, **kwargs)
        if not (request.user.is_staff or request.user.is_superuser):
            return redirect('home-page')


        return data


class NotApprovedContent:

    def dispatch(self, request, *args, **kwargs):
        data = super().dispatch(request, *args, **kwargs)
        if not self.object.approved and request.user.pk != self.object.owner.pk and \
                not request.user.is_staff and not request.user.is_superuser:
            return redirect('home-page')


        return data
