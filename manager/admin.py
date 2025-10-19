from django.contrib import admin
from manager.models import Propiedad, TiposPropiedades, OperacionesPropiedades, EstadosPropiedades, Comunas

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
    list_filter = [ 
        'moneda',
        'fecha',
        'amoblado',
        'piscina'
        ]
    search_fields = [
        'titulo', 
        'descripcion', 
        'ubicacion']
    #solo lectura
    readonly_fields = [
        'fecha',
        'slug']
    list_per_page = 10


class TiposPropiedadesAdmin(admin.ModelAdmin):
    list_display = [
        'tipoPropiedad'
    ]
    
class OperacionesPropiedadesAdmin(admin.ModelAdmin):
    list_display = [
        'operacion'
    ]
class EstadosPropiedadesAdmin(admin.ModelAdmin):
    list_display = [
        'estado'
    ]

class ComunasAdmin(admin.ModelAdmin):
    list_display = [
        'comuna'
    ]
admin.site.register(Propiedad, PropiedadAdmin)
admin.site.register(TiposPropiedades, TiposPropiedadesAdmin)
admin.site.register(OperacionesPropiedades, OperacionesPropiedadesAdmin)
admin.site.register(EstadosPropiedades, EstadosPropiedadesAdmin)
admin.site.register(Comunas, ComunasAdmin)