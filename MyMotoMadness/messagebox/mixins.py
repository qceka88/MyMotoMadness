from django.shortcuts import redirect

from MyMotoMadness.messagebox.models import MyMessage


class RestrictAccessMessages:

    def dispatch(self, request, *args, **kwargs):
        data = MyMessage.objects.get(slug=kwargs['slug'])

        if request.user not in [data.to_user, data.from_user] and not request.user.is_superuser:
            return redirect('my message box view', {'slug_user': request.user.slug_user})

        return super().dispatch(request, *args, **kwargs)
