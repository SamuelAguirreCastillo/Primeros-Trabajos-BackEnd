from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategoriaSerializers, RolSerializers, UsuarioSerializers, DistribuidorSerializers, ProductoSerializers, ClienteSerializers, VendedorSerializers, DevolucionSerializers
from .models import Categoria, Rol, Usuario, Distribuidor, Producto, Cliente, Vendedor, Devolucion


# Create your views here.
class CategoriaViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
    
class RolViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Rol.objects.all()
    serializer_class = RolSerializers
    
class UsuarioViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

class DistribuidorViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Distribuidor.objects.all()
    serializer_class = DistribuidorSerializers    

class ProductoViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers

class ClienteViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers

class VendedorViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializers

class DevolucionViewSet(viewsets.ModelViewSet):
    # Datos  a consultar
    queryset = Devolucion.objects.all()
    serializer_class = DevolucionSerializers

    

