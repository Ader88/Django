from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Math
from .forms import ResultForm
from django.core.paginator import Paginator

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
    operation = request.GET.get('operation')
    maths = Math.objects.all()

    if operation:
        maths = Math.objects.filter(operation=operation)

    paginator = Paginator(maths, 5)
    page_number = request.GET.get('page')
    maths = paginator.get_page(page_number)

    return render(
       request=request,
       template_name="maths/list.html",
       context={"maths": maths, "operation": operation}
    )

def add_result(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maths_list_url')
    else:
        form = ResultForm()
    return render(request, 'add_result.html', {'form': form})