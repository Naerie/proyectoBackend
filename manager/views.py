from django.shortcuts import render
from datos import propiedades
from datos import clientes
from datos import tiposPropiedad, estadosPropiedad
from django.contrib.auth import logout
from django.shortcuts import redirect
from datos import contacto, subs

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
    return render(request, 'templatesApp/contacto-admin.html', {'contacto':contacto})

def gestionar(request):
    return render(request, 'templatesApp/gestionar.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login-admin')

def Interes(request):
    return render(request, 'templatesApp/interes.html', {'clientes':clientes})

def verSubscripciones(request):
    return render(request, 'templatesApp/subscripciones.html', {'subscripciones':subs})