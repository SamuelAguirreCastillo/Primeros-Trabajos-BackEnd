"""agenda URL Configuration

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
from django.contrib.auth.views import logout_then_login,LoginView
from agendaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendar_cita/', views.ingresar_cita),
    path('confirmacion_cita/', views.confirmacion_cita),
    path('filtrar_citas/', views.filtrar_citas),
    path('mostrar_citas/', views.tabla_citas),
    path('login/', LoginView.as_view(template_name='agendaApp/login.html'),name="login"),
    path('inicio/', views.index),
    path('inicio_admin/', views.inicio_admin, name='index'),
    path('preguntas_frecuentes/', views.preguntas_frecuentes),
    path('editar_preguntas_frecuentes/', views.editar_preguntas_frecuentes),
    path('eliminar_pregunta/', views.eliminar_pregunta_frecuente),
    path('confirmar_eliminacion/', views.confirmacion_eliminacion_pregunta),
    path('modificar_pregunta/', views.modificar_pregunta),
    path('confirmar_edit/', views.confirmar_edit),
    path('form_agregar_pregunta/', views.form_agregar_pregunta),
    path('confirmar_agregar_pregunta/', views.confirmar_agregar_pregunta),
    path('eliminar_cita/', views.eliminar_cita),
    path('confirmar_eliminacion_cita/', views.confirmar_eliminacion_cita)

]
