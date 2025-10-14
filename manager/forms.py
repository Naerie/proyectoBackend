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
            'nBanos': 'Número de baños:',                            
            'nHabitaciones': 'Número de habitaciones:',            
            'ubicacion': 'Dirección:',                      
            'superficie': 'Superficie en m²:',            
            'precio': 'Precio:',
            'superficieConstruida': 'Superficie construida en m²:',
            'nEstacionamientos': 'Número de estacionamientos:',  
            'pisosCasa': 'Número de pisos:',          
            'moneda': '',
            'estacionamiento': '',
            'pscina': '',
            'conserje': '',
            'logia': '',
            'amoblado': '',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ingresa el título'
            }),
            'thumb': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona la imagen principal'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',  
                'placeholder': 'Describa la propiedad',
                'rows': 4
            }),
            'nBanos': forms.Select(attrs={
                'class': 'form-select'
            }),
            'nHabitaciones': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: Av. Manuel Montt 123'
            }),
            'superficie': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: 100',
                'min': 0
            }),
            'superficieConstruida': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Ej: 100',
                'min': 0
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',  
                'placeholder': 'Precio',
                'min': 0
            }),
            'moneda': forms.RadioSelect(attrs={
                'class': 'form-check-input'
            }),
            'nEstacionamientos': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pisosCasa': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estacionamiento': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'pscina': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'conserje': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'logia': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'amoblado': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),


        }







