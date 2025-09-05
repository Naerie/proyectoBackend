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
    path('registroPropiedades/', mViews.registro),
    path('propiedades/', mViews.propiedades),
    path('login/', mViews.logIn),
    path('form/', mainViews.formCliente),
    path('home/', mainViews.homeCliente),
    path('manage/',mViews.manage),
    path('', mainViews.index),
    path('nosotros/', mainViews.sobreNosotros),
    path('contacto/',mainViews.contacto)
]
