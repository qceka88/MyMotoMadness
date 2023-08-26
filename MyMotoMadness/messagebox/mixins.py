from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from MyMotoMadness.messagebox.models import MyMessage


class RestrictAccessMessages:

    def dispatch(self, request, *args, **kwargs):
        # try:
        data = MyMessage.objects.get(slug=kwargs['slug'])
        # except ObjectDoesNotExist:
        #     return redirect('home-page')

        if request.user not in [data.to_user, data.from_user] and not request.user.is_superuser:
            return redirect('received list messages view', {'slug_user': request.user.slug_user})
        return super().dispatch(request, *args, **kwargs)
