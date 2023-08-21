from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.forms import modelform_factory
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from MyMotoMadness.messagebox.forms import BaseMessageForm
from MyMotoMadness.messagebox.mixins import RestrictAccessMessages
from MyMotoMadness.messagebox.models import MyMessage

UserModel = get_user_model()


# TODO: check if not registered user try to access message-box
class MessageBoxListView(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    model = MyMessage
    template_name = 'messages/list_messages.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['received_messages'] = MyMessage.objects. \
            filter(to_user=self.request.user) \
            .order_by('send_date')
        data['send_messages'] = MyMessage.objects. \
            filter(from_user=self.request.user) \
            .order_by('send_date')
        return data


class SendMessageView(auth_mixins.LoginRequiredMixin, generic_views.CreateView):
    model = MyMessage
    template_name = 'messages/create_message.html'
    form_class = BaseMessageForm

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        recipient = UserModel.objects.filter(pk=self.kwargs['pk']).get()
        self.extra_context = {
            'recipient': recipient,
        }
        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.from_user = self.request.user
        self.object.to_user = self.extra_context['recipient']
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('my message box view', kwargs={'slug_user': self.request.user.slug_user})


class DetailsMessageView(auth_mixins.LoginRequiredMixin, RestrictAccessMessages, generic_views.DetailView):
    model = MyMessage
    template_name = 'messages/details_message.html'


class DeleteMessageView(auth_mixins.LoginRequiredMixin, RestrictAccessMessages, generic_views.DeleteView):
    model = MyMessage
    template_name = 'messages/delete_message.html'
    form_class = modelform_factory(
        MyMessage,
        fields=(),
    )

    def get(self, request, *args, **kwargs):
        MyMessage.objects.get(slug=kwargs['slug']).delete()
        return redirect('my message box view', {'slug_user': self.request.user.slug_user})
