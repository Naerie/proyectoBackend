from django import forms
from manager.models import Propiedad

class FormRegistrarP(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'
        labels = {'titulo': 'Título de la propiedad',
                'descripcion': 'Descripción',
                'thumb': 'Imagen principal',            
                'carrusel': 'Imágenes adicionales',            
                'nBanos': 'Número de baños',            
                'nHabitaciones': 'Número de habitaciones',            
                'ubicacion': 'Dirección',            
                'comuna': 'Comuna',            
                'tipo': 'Tipo de propiedad',            
                'estado': 'Estado',            
                'superficie': 'Superficie en m²',            
                'precio': 'Precio en CLP'        
                }







