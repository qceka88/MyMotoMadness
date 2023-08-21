from django import forms
from django.contrib import messages
from django.contrib.auth import views as auth_views, mixins as auth_mixins, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as generic_views

from MyMotoMadness.accounts.forms import MotoUserRegisterForm, MotoUserLoginForm, MotoUserChangePassword
from MyMotoMadness.accounts.mixins import CheckForRestriction, CheckForRegisteredUser

UserModel = get_user_model()


class RegisterMotoUser(CheckForRegisteredUser, generic_views.CreateView):
    template_name = 'accounts/register_user.html'
    form_class = MotoUserRegisterForm

    def form_valid(self, form):
        data = super().form_valid(form)
        login(self.request, self.object)
        return data

    def get_success_url(self):
        return reverse_lazy('edit user view', kwargs={'pk': self.object.pk})


class LoginMotoUserView(auth_views.LoginView):
    template_name = 'accounts/login_user.html'
    success_url = reverse_lazy('home-page')
    form_class = MotoUserLoginForm


class LogoutMotoUserView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.success(request, 'Logged out!')
        return super().dispatch(request, *args, **kwargs)


class DetailsMotoUserView(generic_views.DetailView):
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


class EditMotoUser(CheckForRestriction, auth_mixins.LoginRequiredMixin, generic_views.UpdateView):
    template_name = 'accounts/edit_user.html'
    model = UserModel
    form_class = forms.modelform_factory(
        UserModel,
        fields=('first_name', 'last_name', 'email', 'profile_picture', 'phone_number', 'is_staff', 'is_superuser'),
        widgets={
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your first name',
                    'style': "height: 55px",
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your last name',
                    'style': "height: 55px",
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your email',
                    'style': "height: 55px",
                }
            ),
            'phone_number': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your phone number',
                    'style': "height: 55px",
                }
            ),
        },
    )

    def post(self, request, *args, **kwargs):
        context = super().post(request, *args, **kwargs)

        if request.user.pk == self.object.pk and request.user.is_staff:
            self.object.is_staff = request.user.is_staff
            self.object.save()
        return context

    def get_success_url(self):
        return reverse_lazy('details user view', kwargs={'pk': self.object.pk})


class PasswordChange(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change.html'
    model = UserModel
    form_class = MotoUserChangePassword

    def get_success_url(self):
        return reverse_lazy('details user view', kwargs={'pk': self.request.user.pk})


class DeleteMotoUser(CheckForRestriction, generic_views.DeleteView):
    template_name = 'accounts/delete_user.html'
    model = UserModel
    success_url = reverse_lazy('home-page')
