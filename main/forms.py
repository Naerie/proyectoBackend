from django import forms
from main.models import Contacto

class FormContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        labels = {
            'nombre': 'Nombre:',
            'email': 'Correo electrónico:',
            'nTelefono': 'Número de teléfono:',
            'mensaje': 'Mensaje:'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingres tu nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@gmail.com'
            }),
            'nTelefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+56912345678'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 4
            }),
        }
        
