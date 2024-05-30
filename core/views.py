from django.shortcuts import render, redirect
from .forms import OrdenForm, EmpresaForm, ClienteForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def orden(request):
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST)
        empresa_form = EmpresaForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if orden_form.is_valid() and empresa_form.is_valid() and cliente_form.is_valid():
            empresa = empresa_form.save()
            cliente = cliente_form.save()
            orden = orden_form.save(commit=False)
            orden.empresa = empresa
            orden.cliente = cliente
            orden.save()
            return redirect('orden')
    else:
        orden_form = OrdenForm()
        empresa_form = EmpresaForm()
        cliente_form = ClienteForm()
    
    return render(request, 'core/orden.html', {
        'orden_form': orden_form,
        'empresa_form': empresa_form,
        'cliente_form': cliente_form
    })


def login(request):
    return render(request, 'core/login.html')
