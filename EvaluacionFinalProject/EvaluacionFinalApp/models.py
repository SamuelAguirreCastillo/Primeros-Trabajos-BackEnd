from django.db import models

# Create your models here

class Categoria(models.Model):
    tipo = models.CharField(max_length=50)


class Rol(models.Model):
    tipo = models.CharField(max_length=80)


class Usuario(models.Model):
    email = models.EmailField(max_length=120, null=False, unique=True)
    contrasena = models.CharField(max_length=120, null=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=False)

class Distribuidor(models.Model):
    nombre = models.CharField(max_length=80)
    region = models.CharField(max_length=80)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    

class Cliente(models.Model):
    rut = models.CharField(max_length=10, null=False, unique=True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)


class Vendedor(models.Model):
    rut = models.CharField(max_length=10, null=False, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=80)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)


class Devolucion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidor, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    valor = models.PositiveIntegerField()
    detalle = models.CharField(max_length=200)
