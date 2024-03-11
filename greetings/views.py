from django.http import HttpResponse

def greet(request, name=None):
    if name:
        greeting = f"Hello {name.capitalize()}!"
    else:
        greeting = "Hello World!"
    return HttpResponse(greeting)
