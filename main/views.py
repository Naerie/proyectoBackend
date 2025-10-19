from django.shortcuts import render ,redirect,get_object_or_404
from django.http import JsonResponse
from main import forms
from manager.models import Propiedad

#datos.py
from datos import about


# Create your views here.
def index(request):
    propiedades = Propiedad.objects.all().order_by('-fecha')
    # subscripcion
    formulario = forms.FormSuscripcion()
    if request.method =='POST':
        formulario = forms.FormSuscripcion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('home')
    data = {
        'propiedades': propiedades,
        'form':formulario
    }
    
    return render(request, 'templatesMain/home.html', data)

def propiedad(request, slug):
    propiedad = get_object_or_404(Propiedad, slug=slug)
    formulario = forms.FormCliente()
    if request.method == 'POST':
        formulario = forms.FormCliente(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('c-success')
    data ={
        'propiedad':propiedad,
        'form':formulario
    }
    return render(request, 'templatesMain/propiedad.html', data)

def sobreNosotros(request):
    return render (request, 'templatesMain/nosotros.html', about)


def contacto(request):
    formulario = forms.FormContacto()
    if request.method == 'POST':
        formulario = forms.FormContacto(request.POST)
        if formulario.is_valid():
            print('formulario de contacto valido')
            formulario.save()
            return redirect('c-success')    
    data = {'form' : formulario}
    return render(request, 'templatesMain/contacto.html', data)


def contactoSuccess(request):
    return render(request, 'templatesMain/contacto-success.html')

