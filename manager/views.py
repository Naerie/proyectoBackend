from django.shortcuts import render
from datos import propiedades

# Create your views here.
def registro(request):
    return render(request, 'templatesApp/registrarPropiedades.html')

def verPropiedades(request):
    return render(request, 'templatesApp/propiedades.html', {'propiedades':propiedades})

def logIn(request):
    return render(request, 'templatesApp/login.html')

def homeManager(request):
    return render(request, 'templatesApp/manage.html')

def verMensajes(request):
    return render(request, 'templatesApp/contacto-admin.html')