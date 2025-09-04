from django.shortcuts import render

# Create your views here.
def registro(request):
    return render(request, 'templatesApp/registrarPropiedades.html')

def propiedades(request):
    return render(request, 'templatesApp/propiedades.html')

def logIn(request):
    return render(request, 'templatesApp/login.html')