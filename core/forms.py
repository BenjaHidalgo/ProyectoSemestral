from django import forms
from .models import Orden, Empresa, Cliente

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['numero_orden', 'fecha_orden', 'empresa', 'cliente']
        widgets = {
            'fecha_orden': forms.DateInput(attrs={'type': 'date'}),
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['rut', 'razon_social', 'direccion', 'telefono', 'correo', 'sitio_web', 'tipo_servicio']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre_razon_social', 'direccion', 'telefono', 'correo']