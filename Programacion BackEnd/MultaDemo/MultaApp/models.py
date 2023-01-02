from django.db import models

# Create your models here.
class Multa(models.Model):
    nombre = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=3,decimal_places=2)

class Infractor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    celular = models.PositiveIntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    detalles = models.CharField(max_length=300)
    multa = models.ForeignKey(Multa, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=1, default=0)
