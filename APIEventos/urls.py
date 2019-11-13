"""APIEventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('', include('eventos.urls')),
    path('', include('evento_prueba.urls')),
    path('',include('departamento.urls')),
    path('', include('tipolocalidad.urls')),
    path('', include('localidades.urls')),
    path('', include('asientos.urls')),
    path('', include('usuarios.urls')),
    path('', include('pagos.urls')),
    path('',include('imagenes.urls')),
    path('', include('imagenusuario.urls')),
    path('',include('comentarios.urls')),
    path('',include('usuarios.urls')),
    path('',include('detalleevento.urls')),
    path('', include('pagosevento.urls')),
    path('admin/', admin.site.urls),
  
]
