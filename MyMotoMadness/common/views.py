from django.views import generic as views


# Create your views here.
class IndexView(views.TemplateView):
    template_name = 'index.html'
