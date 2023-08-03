from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as generic_views

from MyMotoMadness.accounts.froms import MotoUserRegisterForm, MotoUserLoginForm

UserModel = get_user_model()


class RegisterMotoUser(generic_views.CreateView):
    template_name = 'accounts/register_user.html'
    form_class = MotoUserRegisterForm
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        data = super().form_valid(form)
        login(self.request, self.object)
        return data


class LoginMotoUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'
    success_url = reverse_lazy('home-page')
    form_class = MotoUserLoginForm


class LogoutMotoUserView(auth_views.LogoutView):
    ...


class DetailsMotoUserView(auth_mixins.LoginRequiredMixin, generic_views.DetailView):
    template_name = 'accounts/detail_user.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user_sale_offers'] = []
        for queryset_offers in (
                context['object'].motoparts_set.all(),
                context['object'].motoequipmentgear_set.all(),
                context['object'].motorcycles_set.all()
        ):
            context['user_sale_offers'].extend(queryset_offers)

        return context

