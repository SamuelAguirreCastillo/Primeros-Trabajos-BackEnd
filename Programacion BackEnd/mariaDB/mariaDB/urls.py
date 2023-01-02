"""mariaDB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from mariaDBApp.views import reservaData, renderFormulario, agregarReserva, eliminarReserva, actualizarReserva, vistaInicial, reserva_actualizada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/', vistaInicial),
    path('lista/', reservaData),
    path('formulario/', renderFormulario),
    path('agregar/', agregarReserva),
    path('eliminar_reserva/<id>/', eliminarReserva),
    path('actualizar_reserva/<int:id>', actualizarReserva),
    path('reserva_actualizada/', reserva_actualizada)

]
