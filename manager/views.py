from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.shortcuts import redirect
from manager import forms
from main.models import Contacto, Cliente
from manager.models import Propiedad


#archivo datos.py ir reemplazando 
#from datos import propiedades
# from datos import clientes
from datos import tiposPropiedad, estadosPropiedad, comuna
from datos import subs


def registro(request):
    formulario = forms.FormRegistrarP()
    if request.method == 'POST':
        formulario = forms.FormRegistrarP(request.POST, request.FILES)
        if formulario.is_valid():
            print('formulario de registro de propiedades valido')
            formulario.save()
            return redirect('home-manager')
    data = {'form' : formulario}
    return render(request, 'templatesManager/registrarPropiedades.html', data)


def verPropiedades(request):
    propiedades = []
    for prop in Propiedad.objects.all():
        propiedades.append({
            'obj': prop,
            'form': forms.FormRegistrarP(instance=prop)  # formulario precargado
        })

    return render(request, 'templatesManager/propiedades.html', {
        'propiedades': propiedades
    })


def actualizarPropiedades(request, id):
    # ACTUALIZAR
    propiedad = get_object_or_404(Propiedad, id=id)
    if request.method == 'POST':
        form = forms.FormRegistrarP(request.POST, request.FILES, instance=propiedad)
        if form.is_valid():
            form.save()
            return redirect('listado-propiedades') 
    else:
        form = forms.FormRegistrarP(instance=propiedad)

    data = {'form' : form,
            'propiedad':propiedad}
    return render(request, 'templatesManager/propiedades.html', data)

def logIn(request):
    return render(request, 'templatesManager/login.html')

def homeManager(request):
    return render(request, 'templatesManager/manage.html')

def verMensajes(request):
    contacto = Contacto.objects.all()
    return render(request, 'templatesManager/contacto-admin.html', {'contacto':contacto})

def gestionar(request):
    return render(request, 'templatesManager/gestionar.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login-admin')

def Interes(request):
    clientes = Cliente.objects.all()
    return render(request, 'templatesManager/interes.html', {'clientes':clientes})

def verSubscripciones(request):
    return render(request, 'templatesManager/subscripciones.html', {'subscripciones':subs})