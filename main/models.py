from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    nTelefono = models.CharField(max_length=15,blank=False)
    mensaje = models.TextField(blank=False)
    fecha = models.DateField(auto_now_add=True)

class Cliente(models.Model):
    nombreCliente = models.CharField(max_length= 50, blank =False)
    emailCliente = models.EmailField(max_length=50)
    nTelefonoCliente = models.CharField(max_length=15,blank=False)
    fechaCliente = models.DateField(auto_now_add=True)

class Suscripcion(models.Model):
    emailSus = models.EmailField(max_length=50, blank =False, unique=True)
    fechaSus = models.DateField(auto_now_add=True)
    estadoSus = models.BooleanField(default=True)