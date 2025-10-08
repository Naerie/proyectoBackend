from django.shortcuts import render
from datos import propiedades
from datos import clientes
from datos import tiposPropiedad, estadosPropiedad, comuna
from django.contrib.auth import logout
from django.shortcuts import redirect
from datos import contacto, subs

# Create your views here.
def registro(request):
    contexto = {
        'tipos_inmueble': tiposPropiedad,
        'estado': estadosPropiedad,
        'comuna': comuna
    }
    return render(request, 'templatesManager/registrarPropiedades.html', contexto)

def verPropiedades(request):
    return render(request, 'templatesManager/propiedades.html', {'propiedades':propiedades})

def logIn(request):
    return render(request, 'templatesManager/login.html')

def homeManager(request):
    return render(request, 'templatesManager/manage.html')

def verMensajes(request):
    return render(request, 'templatesManager/contacto-admin.html', {'contacto':contacto})

def gestionar(request):
    return render(request, 'templatesManager/gestionar.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login-admin')

def Interes(request):
    return render(request, 'templatesManager/interes.html', {'clientes':clientes})

def verSubscripciones(request):
    return render(request, 'templatesManager/subscripciones.html', {'subscripciones':subs})