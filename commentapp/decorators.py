from django.http import HttpResponseForbidden

from articleapp.models import Article

# 본인 확인 작업의 Decorator
from commentapp.models import Comment


def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])
        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated