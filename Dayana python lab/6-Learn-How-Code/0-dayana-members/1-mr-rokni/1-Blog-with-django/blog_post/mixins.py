from django.shortcuts import redirect


class customLoginRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login')
        return super(customLoginRequiredMixin, self).dispatch(request, *args, **kwargs)