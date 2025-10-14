from django import forms
import re
from main.models import Contacto


class FormContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        exclude = ['fecha']
        labels = {
            'nombre': 'Nombre:',
            'email': 'Correo electrónico:',
            'nTelefono': 'Número de teléfono:',
            'mensaje': 'Mensaje:'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingresa tu nombre'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@gmail.com'
            }),
            'nTelefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: +56912345678'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 4
            }),
        }

        #validaciones
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            pat = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.fullmatch(pat, email):
                raise forms.ValidationError("Dirección de correo inválida.")
        return email
            
    def clean_nTelefono(self):
        telefono = self.cleaned_data.get('nTelefono')
        if telefono:
            pat = r'^\+\d{1,3}\d{10}$'
            if not re.fullmatch(pat, telefono):
                raise forms.ValidationError('Numero de telefono inválido.')
        return telefono
