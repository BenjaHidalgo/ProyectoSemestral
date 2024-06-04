from django.shortcuts import render, redirect
from .forms import OrdenForm, EmpresaForm, ClienteForm, ProductoForm  # Importar el formulario de productos
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Empresa

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def orden(request):
    listarEmpresa = Empresa.objects.all()
    if request.method == 'POST':
        orden_form = OrdenForm(request.POST)
        
        cliente_form = ClienteForm(request.POST)
        producto_form = ProductoForm(request.POST)
        
        if orden_form.is_valid()  and cliente_form.is_valid() and producto_form.is_valid():
            
            cliente = cliente_form.save()
            producto = producto_form.save()

            # Primero guardamos la orden sin confirmarla para poder establecer las relaciones
            orden = orden_form.save(commit=False)
            orden.cliente = cliente
            # Para la relación ManyToMany con Producto, necesitamos guardar la orden primero
            orden.save()
            orden.productos.add(producto)
            
            return redirect('core/index.html')  # Redirige al usuario a la página de éxito
        else:
            print(orden_form.errors)
            print(cliente_form.errors)
            print(producto_form.errors)
    else:
        orden_form = OrdenForm()

        cliente_form = ClienteForm()
        producto_form = ProductoForm()

    context = {
        'orden_form': orden_form,
        'listado': listarEmpresa,
        'cliente_form': cliente_form,
        'producto_form': producto_form,
    }
    return render(request, 'core/orden.html', context)



def login(request):
    return render(request, 'core/login.html')
