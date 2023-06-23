from django.db import models

class Participante(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha = models.DateField()
    empleador = models.CharField(max_length=50)
    correo = models.EmailField()
    profesion = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=200, blank=True)