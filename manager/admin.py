from django.contrib import admin
from manager.models import Propiedad

# Register your models here.

class PropiedadAdmin(admin.ModelAdmin):
    list_display =[
        'titulo',
        'thumb',
        'descripcion',
        'nHabitaciones',
        'nBanos',
        'superficie',
        'superficieConstruida',
        'ubicacion',
        'precio',
        'moneda',
        'fecha',
        'conserje',
        'logia',
        'amoblado',
        'estacionamiento',
        'nEstacionamientos',
        'piscina'
    ]

admin.site.register(Propiedad, PropiedadAdmin)