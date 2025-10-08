from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nTelefono = models.CharField(max_length=12)
    mensaje = models.TextField()