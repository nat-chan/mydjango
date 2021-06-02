from django.http import Http404
from django.template.response import TemplateResponse
from blog.models import Post

def post_list(request):
    return TemplateResponse(
        request, "post_list.html",
        {"posts": Post.objects.all()}
    )


def post_detail(request, post_id):
    return TemplateResponse(
        request, "post_list.html",
        {"posts": Post.objects.all()}
    )
