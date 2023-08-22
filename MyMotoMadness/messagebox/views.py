from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.forms import modelform_factory
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from MyMotoMadness.messagebox.forms import CreateMessageForm
from MyMotoMadness.messagebox.mixins import RestrictAccessMessages
from MyMotoMadness.messagebox.models import MyMessage

UserModel = get_user_model()


class MessageBoxListView(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    model = MyMessage
    template_name = 'messages/list_messages.html'

    @staticmethod
    def get_messages_for_user(data, current_user):
        data['received_messages'] = []
        data['send_messages'] = []

        for msg in data['object_list']:
            if msg.to_user == current_user and not msg.receiver_delete:
                if not msg.viewed:
                    msg.viewed = True
                    msg.save()
                data['received_messages'].append(msg)

            elif msg.from_user == current_user and not msg.sender_delete:
                data['send_messages'].append(msg)

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return self.get_messages_for_user(context, self.request.user)


class SendMessageView(auth_mixins.LoginRequiredMixin, generic_views.CreateView):
    model = MyMessage
    template_name = 'messages/create_message.html'
    form_class = CreateMessageForm

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

        return redirect('my message box view', {'slug_user': self.request.user.slug_user})
