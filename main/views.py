from django.shortcuts import render
from datos import propiedades
from datos import about
from django.http import JsonResponse
from datos import operacionPropiedad, tiposPropiedad, comuna


# Create your views here.
def index(request):
    contexto = {
        'propiedades': propiedades,
        'operacion': operacionPropiedad,
        'tipos_inmueble': tiposPropiedad,
        'comuna': comuna
    }
    
    return render(request, 'templatesApp/home.html', contexto)


def sobreNosotros(request):
    return render (request, 'templatesApp/nosotros.html', about)

def contacto(request):
    return render (request, 'templatesApp/contacto.html')

def propiedad(request):
    return render(request, 'templatesApp/propiedad.html', {'propiedades':propiedades})