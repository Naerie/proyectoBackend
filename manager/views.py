from django.shortcuts import render
from datos import propiedades
from datos import tiposPropiedad, estadosPropiedad


# Create your views here.
def registro(request):
    contexto = {
        'tipos_inmueble': tiposPropiedad,
        'estado': estadosPropiedad
    }
    return render(request, 'templatesApp/registrarPropiedades.html', contexto)

def verPropiedades(request):
    return render(request, 'templatesApp/propiedades.html', {'propiedades':propiedades})

def logIn(request):
    return render(request, 'templatesApp/login.html')

def homeManager(request):
    return render(request, 'templatesApp/manage.html')

def verMensajes(request):
    return render(request, 'templatesApp/contacto-admin.html')

def gestionar(request):
    return render(request, 'templatesApp/gestionar.html')