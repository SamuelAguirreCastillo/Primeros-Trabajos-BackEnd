from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Reserva(models.Model):
    nombre = models.CharField(max_length= 50)
    telefono = models.PositiveIntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad = models.PositiveIntegerField()
    observacion = models.CharField(max_length=200)

