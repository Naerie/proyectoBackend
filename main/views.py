from django.shortcuts import render
from datos import propiedades
from datos import about
from django.http import JsonResponse
from datos import operacionPropiedad, tiposPropiedad, comuna
from main import forms


# Create your views here.
def index(request):
    contexto = {
        'propiedades': propiedades,
        'operacion': operacionPropiedad,
        'tipos_inmueble': tiposPropiedad,
        'comuna': comuna
    }
    
    return render(request, 'templatesMain/home.html', contexto)


def sobreNosotros(request):
    return render (request, 'templatesMain/nosotros.html', about)

""" def contacto(request):
    return render (request, 'templatesMain/contacto.html') """

def contacto(request):
    formulario =forms.FormContacto()
    data = {'form' : formulario}
    return render(request, 'templatesMain/contacto.html', data)

def propiedad(request):
    return render(request, 'templatesMain/propiedad.html', {'propiedades':propiedades})