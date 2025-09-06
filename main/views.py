from django.shortcuts import render

# Create your views here.
def formCliente(request):
    return render (request, 'templatesApp/cliente.html')

def index(request):
    propiedades =[
        {
            'titulo':'Casa 1',
            'imagen':'assets/img/placeholder-card.jpeg',
            'descripcion':'100mt2, lorem ipsun'
        }
    ]
    return render (request, 'templatesApp/home.html', {"propiedades":propiedades})

def sobreNosotros(request):
    return render (request, 'templatesApp/nosotros.html')

def contacto(request):
    return render (request, 'templatesApp/contacto.html')
