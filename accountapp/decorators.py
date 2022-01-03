from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# 본인 확인 작업의 Decorator
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated