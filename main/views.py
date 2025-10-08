from django.shortcuts import render ,redirect
from datos import propiedades
from datos import about
from django.http import JsonResponse
from datos import operacionPropiedad, tiposPropiedad, comuna
from main import forms


# Create your views here.
def index(request):
    data = {
        'propiedades': propiedades,
        'operacion': operacionPropiedad,
        'tipos_inmueble': tiposPropiedad,
        'comuna': comuna,
    }
    
    return render(request, 'templatesMain/home.html', data)


def sobreNosotros(request):
    return render (request, 'templatesMain/nosotros.html', about)


def contacto(request):
    formulario = forms.FormContacto()
    if request.method == 'POST':
        formulario = forms.FormContacto(request.POST)
        if formulario.is_valid():
            print('formulario de contacto valido')
            formulario.save()
            return redirect('home')    
    data = {'form' : formulario}
    return render(request, 'templatesMain/contacto.html', data)

def propiedad(request):
    return render(request, 'templatesMain/propiedad.html', {'propiedades':propiedades})