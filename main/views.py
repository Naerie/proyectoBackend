from django.shortcuts import render
from datos import propiedades
# Create your views here.
def index(request):
    propiedades
    return render (request, 'templatesApp/home.html', {"propiedades":propiedades})

def sobreNosotros(request):
    return render (request, 'templatesApp/nosotros.html')

def contacto(request):
    return render (request, 'templatesApp/contacto.html')

def propiedad(request):
    return render(request, 'templatesApp/propiedad.html', {'propiedades':propiedades})