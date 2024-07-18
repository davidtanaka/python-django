from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.
def blog(request):
    print('blog')
    return HttpResponse('Blog do app 1')

def exemplo(resquest):
    return HttpResponse('Exemplo do blog 1')