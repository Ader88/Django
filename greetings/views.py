from django.http import HttpResponse
from django.shortcuts import render

def greet(request):
    greeting = "Hello World!"
    return HttpResponse(greeting)

def greet_name(request, name):
    greeting = f"Hello {name.capitalize()}!"
    return HttpResponse(greeting)

def welcome(request):
    return render(request, 'greetings/welcome.html')

def about(request):
    return render(request, 'greetings/about.html')

def contact(request):
    return render(request, 'greetings/contact.html')