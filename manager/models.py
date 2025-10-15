from django.db import models

# Create your models here.
class Propiedad(models.Model):
    MONEDAS = [
        ('UF', 'UF'),
        ('CLP', '$'),
    ]

    CANTIDADES = [(i, str(i)) for i in range(1, 11)] + [(11, '10+')]

    titulo = models.CharField(max_length=50, blank=False)
    thumb = models.ImageField(blank=False)
    descripcion = models.TextField()
    nHabitaciones = models.IntegerField(choices=CANTIDADES, default=1)
    nBanos = models.IntegerField(choices=CANTIDADES, default=1)
    superficie = models.FloatField()
    superficieConstruida = models.FloatField()
    ubicacion = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)
    moneda = models.CharField(max_length=3, choices=MONEDAS, default='CLP')
    fecha = models.DateField(auto_now_add=True)
    #EXTRAS
        #Depto
    conserje = models.BooleanField(default=False)
    logia = models.BooleanField(default=False)
    amoblado = models.BooleanField(default=False)
        #Ambos
    estacionamiento = models.BooleanField(default=False)
    nEstacionamientos = models.IntegerField(choices=CANTIDADES, default=1)
    piscina = models.BooleanField(default=False)



