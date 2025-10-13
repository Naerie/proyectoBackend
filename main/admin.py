from django.contrib import admin
from main.models import Contacto
# Register your models here.

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'nTelefono', 'mensaje']

admin.site.register(Contacto, ContactoAdmin)
