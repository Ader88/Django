from django.shortcuts import render
from django.http import HttpResponse
from .models import Math
from .forms import ResultForm

# Create your views here.

def add(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a + b)

def sub(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a - b)

def mul(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a * b)

def div(request, a, b):
    a, b = int(a), int(b)
    if b == 0:
        return HttpResponse("Nie dziel przez 0")
    return HttpResponse(a / b)

def maths_list(request):
    maths = Math.objects.all()
    return render(request, 'maths_list.html', {'maths': maths})

def add_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maths_list_url')
    else:
        form = ResultForm()
    return render(request, 'add_result.html', {'form': form})