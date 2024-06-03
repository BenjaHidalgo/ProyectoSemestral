from django import forms
from .models import Orden, Empresa, Cliente, Producto

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
        widgets = {
            'rut': forms.TextInput(attrs={'required': True}),
            'razon_social': forms.TextInput(attrs={'required': True}),
            'direccion': forms.TextInput(attrs={'required': True}),  
            'telefono': forms.TextInput(attrs={'required': True}), 
            'correo': forms.TextInput(attrs={'required': True}), 
            'sitio_web': forms.TextInput(attrs={'required': True}), 
            'tipo_servicio': forms.TextInput(attrs={'required': True}), 
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre_razon_social', 'direccion', 'telefono', 'correo']
        widgets = {
            'rut': forms.TextInput(attrs={'required': True}),
            'nombre_razon_social': forms.TextInput(attrs={'required': False}),
            'direccion': forms.TextInput(attrs={'required': True}),  
            'telefono': forms.TextInput(attrs={'required': False}), 
            'correo': forms.TextInput(attrs={'required': True}),  
        }


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo_producto', 'nombre_producto', 'cantidad', 'precio_unitario']