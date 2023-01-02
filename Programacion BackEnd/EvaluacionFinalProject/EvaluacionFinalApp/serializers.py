# Importación de serializers
from rest_framework import serializers
# Importación de clases
from .models import Categoria, Rol, Usuario, Distribuidor, Producto, Cliente, Vendedor, Devolucion

# Clase de serialización
class CategoriaSerializers(serializers.HyperlinkedModelSerializer):
    # Clase de modelo y campos a exponer
    class Meta:
        model = Categoria
        fields = '__all__'

class RolSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class DistribuidorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distribuidor
        fields = '__all__'

class ProductoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VendedorSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class DevolucionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devolucion
        fields = '__all__'
