from django.db import models


class Empresa(models.Model):
    rut = models.CharField(max_length=12)
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    sitio_web = models.URLField(blank=True, null=True)
    tipo_servicio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.razon_social

class Cliente(models.Model):
    rut = models.CharField(max_length=12)
    nombre_razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre_razon_social

class Orden(models.Model):
    numero_orden = models.CharField(max_length=10)
    fecha_orden = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.numero_orden
    

    
