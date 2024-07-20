from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request):
    context = {
        'text': 'Você está no blog', 
        'title': 'Essa página é um exemplo - '
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