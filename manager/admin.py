from django.contrib import admin
from manager.models import Propiedad

# Register your models here.

class PropiedadAdmin(admin.ModelAdmin):
    list_display =[
        'titulo',
        'thumb',
        'nBanos',
        'nHabitaciones',
        'superficie',
        'ubicacion',
        'precio',
        'descripcion'
    ]

admin.site.register(Propiedad, PropiedadAdmin)