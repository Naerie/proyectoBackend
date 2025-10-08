from django.db import models

# Create your models here.
class Propiedad(models.Model):
    titulo = models.CharField(max_length=50)
    thumb = models.ImageField()
    carrusel = models.ImageField()
    nBanos = models.IntegerField()
    nHabitaciones = models.IntegerField()
    superficie = models.FloatField()
    ubicacion = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=50) 
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()