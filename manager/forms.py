from django import forms
from manager.models import Propiedad, TiposPropiedades, OperacionesPropiedades, EstadosPropiedades, Comunas

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
            'superficie': 'Superficie total:',            
            'precio': 'Precio:',
            'superficieConstruida': 'Superficie construida:',
            'nEstacionamientos': 'Número de estacionamientos:',  
            'moneda': '',
            'estacionamiento': 'Estacionamiento',
            'piscina': 'Piscina',
            'conserje': 'Conserje',
            'logia': 'Logia',
            'amoblado': 'Amoblado'
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
            'estacionamiento': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'piscina': forms.CheckboxInput(attrs={
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


class FormTiposPropiedades(forms.ModelForm):
    class Meta:
        model = TiposPropiedades
        fields = '__all__'
        labels = {'tipoPropiedad':''}
        widgets = {'tipoPropiedad':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nuevo tipo de propiedad'
            }),
            }
    def clean_tipoPropiedades(self):
        tipo = self.cleaned_data.get('tipoPropiedad')
        if TiposPropiedades.objects.filter(tipoPropiedad=tipo).exists():
            raise forms.ValidationError("Ya existe en la base de datos")
        return tipo

class FormEstadosPropiedades(forms.ModelForm):
    class Meta:
        model = EstadosPropiedades
        fields = '__all__'
        labels = {'estado':''}
        widgets = {'estado':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nueva disponibilidad'
            }),
            }
    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if EstadosPropiedades.objects.filter(estado=estado).exists():
            raise forms.ValidationError("Ese registro ya existe en la base de datos")
        return estado

class FormOperacionesPropiedades(forms.ModelForm):
    class Meta:
        model = OperacionesPropiedades
        fields = '__all__'
        labels = {'operacion':''}
        widgets = {'operacion':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nueva operación'
            }),
            }
    def clean_operación(self):
        operacion = self.cleaned_data.get('operacion')
        if OperacionesPropiedades.objects.filter(operacion=operacion).exists():
            raise forms.ValidationError("Ese registro ya existe en la base de datos")
        return operacion

class FormComunas(forms.ModelForm):
    class Meta:
        model = Comunas
        fields = '__all__'
        labels = {'comuna':''}
        widgets = {'comuna':forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nueva comuna'
            }),
            }
    def clean_comuna(self):
        comuna = self.cleaned_data.get('comuna')
        if Comunas.objects.filter(comuna=comuna).exists():
            raise forms.ValidationError("Ese registro ya existe en la base de datos")
        return comuna




