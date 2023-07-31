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


class LoginMotoUser(auth_views.LoginView):
    template_name = 'accounts/login_user.html'
    success_url = reverse_lazy('home-page')
    form_class = MotoUserLoginForm


class LogoutMotoUser(auth_views.LogoutView):
    ...
