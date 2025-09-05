from django.shortcuts import render

# Create your views here.
def formCliente(request):
    return render (request, 'templatesApp/cliente.html')

def homeCliente(request):
    return render (request, 'templatesApp/home.html')

def index(request):
    return render (request, 'templatesApp/index.html')

def sobreNosotros(request):
    return render (request, 'templatesApp/nosotros.html')

def contacto(request):
    return render (request, 'templatesApp/contacto.html')
