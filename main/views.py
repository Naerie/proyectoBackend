from django.shortcuts import render
from datos import propiedades
from about import about

# Create your views here.
def index(request):
    return render (request, 'templatesApp/home.html', {"propiedades":propiedades})

def sobreNosotros(request):
    return render (request, 'templatesApp/nosotros.html', about)

def contacto(request):
    return render (request, 'templatesApp/contacto.html')

def propiedad(request):
    return render(request, 'templatesApp/propiedad.html', {'propiedades':propiedades})