from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.
def myView(request):
    print('Home')
    return HttpResponse('Blog do app')
