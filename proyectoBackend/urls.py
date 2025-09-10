"""
URL configuration for proyectoBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manager import views as mViews
from main import views as mainViews

urlpatterns = [
    path('admin/', admin.site.urls),
    # cliente
    path('', mainViews.index, name="home"),
    path('nosotros/', mainViews.sobreNosotros, name="about"),
    path('contacto/',mainViews.contacto, name="contacto"),
    path('propiedad/', mainViews.propiedad, name='propiedad'),

    # admin
    path('login/', mViews.logIn, name="login-admin"),
    path('manage/',mViews.homeManager, name='home-manager'),
    path('registroPropiedades/', mViews.registro, name="registro-propiedades"),
    path('propiedades/', mViews.verPropiedades, name="listado-propiedades"),
    path('mensajes/', mViews.verMensajes, name='ver-contacto'),
    path('gestion/', mViews.gestionar, name='gestion')
]
