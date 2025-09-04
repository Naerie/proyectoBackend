from django.shortcuts import render

# Create your views here.
def formCliente(request):
    return render (request, 'templatesApp/cliente.html')
