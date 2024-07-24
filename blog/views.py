from django.shortcuts import render
from blog.data import posts
# Create your views here.
def blog(request):
    context = {
        'title': 'Essa página é um exemplo - ',
        'posts': posts
    }

    print('blog')
    return render(
        request,
        'blog/index.html',
        context=context
    )

def exemplo(request):
    context_exemplo = {'text': 'Você está vendo um exemplo'}

    return render(
        request,
        'blog/exemplo.html',
        context=context_exemplo
    )