from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.urls import reverse_lazy
from django.views import generic as generic_views

from MyMotoMadness.messagebox.forms import BaseMessageForm
from MyMotoMadness.messagebox.models import MyMessage

UserModel = get_user_model()


# Create your views here.
class MessageBoxListView(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    model = MyMessage
    template_name = 'messages/list_messages.html'


class SendMessageView(auth_mixins.LoginRequiredMixin, generic_views.CreateView):
    model = MyMessage
    template_name = 'messages/create_message.html'
    form_class = BaseMessageForm
    success_url = reverse_lazy('list messages view')

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
