from django.http import Http404, HttpRequest
from django.shortcuts import render
from blog.data import posts
from typing import Any

# Create your views here.
def blog(request):
    context = {
        'title': 'Essa página é um exemplo - ',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context=context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')

    context = {
        'post': found_post,
        'title': found_post['title'] + ' - '
    }

    return render(
        request,
        'blog/post.html',
        context=context
    )


def exemplo(request):
    context_exemplo = {'text': 'Você está vendo um exemplo'}

    return render(
        request,
        'blog/exemplo.html',
        context=context_exemplo
    )