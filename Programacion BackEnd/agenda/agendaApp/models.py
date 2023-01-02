from django.db import models

# Create your models here.


class PersonaCita(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length = 100)
    email = models.CharField(max_length=100)
    celular = models.PositiveIntegerField()
    fecha = models.DateField()
    hora = models.CharField(max_length=10)
    motivo = models.CharField(max_length=400)


class PreguntaFrecuente(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)