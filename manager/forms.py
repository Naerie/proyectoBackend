from django import forms
from manager.models import Propiedad

class FormRegistrarP(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'
        labels = {
            'titulo': 'Título de la propiedad:',
            'descripcion': 'Descripción:',
            'thumb': 'Imagen principal:',            
            'carrusel': 'Imágenes adicionales:',            
            'nBanos': 'Número de baños:',                            
            'nHabitaciones': 'Número de habitaciones:',            
            'ubicacion': 'Dirección:',                      
            'superficie': 'Superficie en m²:',            
            'precio': 'Precio:'        
                }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa el título de la propiedad'
            }),
            'thumb': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona la imagen principal'
            }),
            'carrusel': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona imágenes adicionales',
            }),
            'nBanos': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de baños',
                'min': 0
            }),
            'nHabitaciones': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de habitaciones',
                'min': 0
            }),
            'superficie': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Superficie en m²',
                'min': 0,
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Av. Manuel Montt 123'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Precio',
                'min': 0,
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describa la propiedad',
                'rows': 4
            }),
        }







