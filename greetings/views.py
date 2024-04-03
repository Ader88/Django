from django.http import HttpResponse
from django.shortcuts import render

def greet(request, name=None):
    if name:
        greeting = f"Hello {name.capitalize()}!"
    else:
        greeting = "Hello World!"
    return HttpResponse(greeting)

def welcome(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')