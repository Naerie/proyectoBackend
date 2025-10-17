from django.db import models
from django.utils.text import slugify

# Create your models here.
class Propiedad(models.Model):
    MONEDAS = [
        ('UF', 'UF'),
        ('CLP', '$'),
    ]

    CANTIDADES = [(i, str(i)) for i in range(1, 11)] + [(11, '10+')]
    CANTIDADESEST = [(i, str(i)) for i in range(0, 11)] + [(11, '10+')]


    titulo = models.CharField(max_length=50, blank=False)
    thumb = models.ImageField(blank=False)
    descripcion = models.TextField()
    nHabitaciones = models.IntegerField(choices=CANTIDADES, default=1)
    nBanos = models.IntegerField(choices=CANTIDADES, default=1)
    superficie = models.FloatField(null=True, blank=True)
    superficieConstruida = models.FloatField(null=True, blank=True)
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
    nEstacionamientos = models.IntegerField(choices=CANTIDADESEST, default=0)
    piscina = models.BooleanField(default=False)
    # slug
    slug = models.SlugField(max_length=60, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)




