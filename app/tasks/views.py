from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def teste(request):
    return HttpResponse('Hello World')

def login(request):
    return render(request, 'tasks/login.html')

def testeParam(request, name):
    return render(request, 'tasks/testeParm.html', {'name': name})
