from django.shortcuts import redirect


class CheckUserArticlePermission:

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            return redirect('common articles views')

        data = super().dispatch(request, *args, **kwargs)
        return data
