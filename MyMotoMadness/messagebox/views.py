from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.forms import modelform_factory
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from MyMotoMadness.messagebox.forms import SendMessageForm, CreateMessageForm
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

    def get_context_data(self, **kwargs):
        try:
            return super().get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = len(self.object_list) // self.paginate_by
            return super().get_context_data(**kwargs)


class SentMessagesView(auth_mixins.LoginRequiredMixin, generic_views.ListView):
    model = MyMessage
    template_name = 'messages/sended_messages.html'
    paginate_by = 6

    def get_queryset(self):
        queryset = MyMessage.objects.filter(from_user=self.request.user, sender_delete=False).order_by('-send_date')
        return queryset

    def get_context_data(self, **kwargs):
        try:
            return super().get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = len(self.object_list) // self.paginate_by
            return super().get_context_data(**kwargs)


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
        return reverse_lazy('sent list messages view', kwargs={'slug_user': self.request.user.slug_user})


class CreateNewMessageView(auth_mixins.LoginRequiredMixin, generic_views.CreateView):
    model = MyMessage
    template_name = 'messages/create_new_message.html'
    form_class = CreateMessageForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.from_user = self.request.user
        self.object.to_user = UserModel.objects.get(username=form.cleaned_data['input_user'])
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sent list messages view', kwargs={'slug_user': self.request.user.slug_user})


class DetailReceivedMessageView(auth_mixins.LoginRequiredMixin, RestrictAccessMessages, generic_views.DetailView,
                                generic_views.ListView):
    model = MyMessage
    template_name = 'messages/details_received_message.html'
    paginate_by = 3
    allow_empty = False
    redirect_url = 'received list messages view'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(self.redirect_url, {'slug_user': request.user.slug_user})

    def get_queryset(self):
        self.object_list = MyMessage.objects.filter(to_user=self.request.user,
                                                    receiver_delete=False).order_by('-send_date')
        if self.object_list and self.kwargs['slug'] not in [msg.slug for msg in self.object_list]:
            self.kwargs['slug'] = self.object_list.first().slug

        return self.object_list

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if not self.object.readed and self.object.to_user == self.request.user:
            self.object.readed = True
            if not self.object.viewed:
                self.object.viewed = True
            self.object.save()
        return data


class DetailSentMessageView(auth_mixins.LoginRequiredMixin, RestrictAccessMessages, generic_views.DetailView,
                            generic_views.ListView):
    model = MyMessage
    template_name = 'messages/details_sent_message.html'
    paginate_by = 3
    allow_empty = False
    redirect_url = 'sent list messages view'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(self.redirect_url, {'slug_user': request.user.slug_user})

    def get_queryset(self):
        self.object_list = MyMessage.objects.filter(from_user=self.request.user,
                                                    sender_delete=False).order_by('-send_date')

        if self.object_list and self.kwargs['slug'] not in [msg.slug for msg in self.object_list]:
            self.kwargs['slug'] = self.object_list.first().slug

        return self.object_list


class DeleteMessageView(auth_mixins.LoginRequiredMixin, RestrictAccessMessages, generic_views.DeleteView):
    model = MyMessage
    template_name = 'messages/delete_message.html'
    form_class = modelform_factory(
        MyMessage,
        fields=(),
    )
    redirect_url = 'home-page'

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
        return redirect(request.META['HTTP_REFERER'])
