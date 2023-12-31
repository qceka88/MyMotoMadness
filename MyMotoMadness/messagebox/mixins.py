from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect

from MyMotoMadness.messagebox.forms import SearchMessageForm
from MyMotoMadness.messagebox.models import MyMessage


class RestrictAccessMessages:

    def dispatch(self, request, *args, **kwargs):
        try:
            data = MyMessage.objects.get(slug=kwargs['slug'])
        except ObjectDoesNotExist:
            return redirect(self.redirect_url, {'slug_user': request.user.slug_user})

        if request.user not in [data.to_user, data.from_user] and not request.user.is_superuser:
            return redirect('received list messages view', {'slug_user': request.user.slug_user})
        return super().dispatch(request, *args, **kwargs)

class GetContextDataListMixin:
    def get_context_data(self, **kwargs):
        try:
            data = super().get_context_data(**kwargs)
            data['search_message'] = SearchMessageForm(self.request.GET)
            return data
        except Http404:
            self.kwargs['page'] = len(self.object_list) // self.paginate_by
            data = super().get_context_data(**kwargs)
            data['search_message'] = SearchMessageForm(self.request.GET)
            return data