from django.shortcuts import redirect


class CheckForRestriction:

    def get(self, request, *args, **kwargs):
        if request.user.pk != kwargs['pk'] and not request.user.is_superuser:
            return redirect('home-page')
        else:
            data = super().get(request, *args, **kwargs)
            return data


class CheckForRegisteredUser:

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            return redirect('details user view', pk=request.user.pk)

        else:
            data = super().get(request, *args, **kwargs)
            return data
