from enum import Enum


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
    BONET = 'Bonet'
    BOOTS = 'Boots'
    GLOVES = 'Gloves'
    PROTECTORS = 'Protectors'
    OTHER = 'Other..'

class AddPicturesToSaleOffer:

    @staticmethod
    def add_pictures_to_sale_offer(sale_object, request, owner, SaleImageClass):
        sale_object.owner = owner
        sale_object.save()
        for field in request.FILES.keys():
            for image_file in request.FILES.getlist(field):
                image = SaleImageClass(image=image_file, sale_ad=sale_object)
                image.save()

        return sale_object
