from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.forms import modelform_factory
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from MyMotoMadness.messagebox.forms import SendMessageForm
from MyMotoMadness.messagebox.mixins import RestrictAccessMessages
from MyMotoMadness.messagebox.models import MyMessage

UserModel = get_user_model()


class ReceivedMessagesView(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    model = MyMessage
    template_name = 'messages/received_messages.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = MyMessage.objects.filter(to_user=self.request.user, receiver_delete=False).order_by('-send_date')
        queryset.update(viewed=True)

        return queryset


class SentMessagesView(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    model = MyMessage
    template_name = 'messages/sended_messages.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = MyMessage.objects.filter(from_user=self.request.user, sender_delete=False).order_by('-send_date')

        return queryset


class SendMessageView(auth_mixins.LoginRequiredMixin, generic_views.CreateView):
    model = MyMessage
    template_name = 'messages/send_message.html'
    form_class = SendMessageForm

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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.object.to_user == self.request.user:
            self.object.readed = True
            self.object.save()
        return data


class DeleteMessageView(auth_mixins.LoginRequiredMixin, RestrictAccessMessages, generic_views.DeleteView):
    model = MyMessage
    template_name = 'messages/delete_message.html'
    form_class = modelform_factory(
        MyMessage,
        fields=(),
    )

    @staticmethod
    def check_message_for_deletion(message_object, request):
        if request.user == message_object.from_user and not message_object.sender_delete:
            message_object.sender_delete = True
        elif request.user == message_object.to_user and not message_object.receiver_delete:
            message_object.receiver_delete = True
        message_object.save()

        if message_object.sender_delete and message_object.receiver_delete:
            message_object.delete()

    def get(self, request, *args, **kwargs):
        my_message = MyMessage.objects.get(slug=kwargs['slug'])
        self.check_message_for_deletion(my_message, request)
        a = 'HTTP_REFERER'
        return redirect('received messages view', {'slug_user': self.request.user.slug_user})
