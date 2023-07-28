# Create your views here.
from django.views import generic as views

from MyMotoMadness.saleads.models import MotoGear, MotoParts, Motorcycles

a, b, c = Motorcycles, MotoGear, MotoParts


class CommonSaleView(views.TemplateView):
    template_name = 'sales/sales_common.html'
