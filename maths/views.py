from django.shortcuts import render
from django.http import HttpResponse
from .models import Math
from .forms import ResultForm

# Create your views here.

def add(request, a, b):
    a, b = int(a), int(b)
    result = a + b
    return render(request, 'add.html', {'a': a, 'b': b, 'result': result})

def sub(request, a, b):
    a, b = int(a), int(b)
    result = a - b
    return render(request, 'sub.html', {'a': a, 'b': b, 'result': result})

def mul(request, a, b):
    a, b = int(a), int(b)
    result = a * b
    return render(request, 'mul.html', {'a': a, 'b': b, 'result': result})

def div(request, a, b):
    a, b = int(a), int(b)
    if b == 0:
        return HttpResponse("Nie dziel przez 0")
    result = a / b
    return render(request, 'div.html', {'a': a, 'b': b, 'result': result})

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