from django.db import models

# Create your models here.
class Propiedad(models.Model):
    titulo = models.CharField(max_length=50,blank=False)
    thumb = models.ImageField(blank=False)
    carrusel = models.ImageField()
    nBanos = models.IntegerField(blank=False)
    nHabitaciones = models.IntegerField(blank=False)
    superficie = models.FloatField()
    ubicacion = models.CharField(max_length=50)
    precio = models.CharField(max_length=50)
    descripcion = models.TextField()