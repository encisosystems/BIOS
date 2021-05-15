from django.db import models

# Create your models here.
class Persona(models.Model):
    documento = models.CharField(max_length=30)
    tipo_documento = models.CharField(max_length=30)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)
    cargo = models.CharField(max_length=30)

class Empresa(models.Model):
    nit = models.CharField(max_length=30)
    razon_social = models.PositiveBigIntegerField(default=0)
    telefono = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    descripcion_servicio = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)

class TipoExamen(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)

class TipoConcepto(models.Model):
    codigo = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)


