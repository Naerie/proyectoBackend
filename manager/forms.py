from django import forms

class FormRegistrarP(forms.Form):
    titulo = forms.CharField()
    thumb = forms.ImageField()
    carrusel = forms.ImageField()
    nBaños = forms.IntegerField()
    nHabitaciones = forms.IntegerField()
    superficie = forms.FloatField()
    ubicacion = forms.CharField()
    comuna = forms.CharField() #descubrir si se pueden usar valores de base de dato en un select
    descripcion = forms.CharField()
    tipo = forms.CharField() #same as comuna
    estado = forms.CharField() #same as comuna
    precio = forms.IntegerField(required=False) 

#buscar si se puede poner "alias" o algo para cambiar el texto que se muestra en el form

    titulo.widget.attrs['class'] = "form-control"
    descripcion.widget.attrs['class'] = "form-control"
    thumb.widget.attrs['class'] = "form-control"
    carrusel.widget.attrs['class'] = "form-control"
    nBaños.widget.attrs['class'] = "form-control"
    nHabitaciones.widget.attrs['class'] = "form-control"
    ubicacion.widget.attrs['class'] = "form-control"
    comuna.widget.attrs['class'] = "form-control"
    tipo.widget.attrs['class'] = "form-control"
    estado.widget.attrs['class'] = "form-control"
    superficie.widget.attrs['class'] = "form-control"
    precio.widget.attrs['class'] = "form-control"




