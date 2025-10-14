from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    nTelefono = models.CharField(max_length=12,blank=False)
    mensaje = models.TextField(blank=False)
    fecha = models.DateField(auto_now_add=True)