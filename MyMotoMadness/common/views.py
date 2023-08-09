from django.contrib.auth import get_user_model
from django.views import generic as views

from MyMotoMadness.saleads.models import Motorcycles, MotoParts, MotoEquipmentGear

UserModel = get_user_model()


# Create your views here.
class IndexView(views.TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['bikes_quantity'] = Motorcycles.objects.all().count()
        data['equipment_quantity'] = MotoEquipmentGear.objects.all().count()
        data['parts_quantity'] = MotoParts.objects.all().count()
        data['registered_users'] = UserModel.objects.all().count()

        return data
