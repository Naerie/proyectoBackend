from django.contrib import admin
from main.models import Contacto, Cliente

# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 
                    'email', 
                    'nTelefono', 
                    'mensaje', 
                    'fecha']

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombreCliente',
                    'emailCliente',
                    'nTelefonoCliente',
                    'fechaCliente']
    
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Cliente, ClienteAdmin)
