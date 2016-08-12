from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Posicion(models.Model):
    posicion = models.IntegerField(default=1)
    image = models.ImageField(null=True, blank=True)
    equipo = models.CharField(max_length=120, blank=True)
    partidos = models.IntegerField(default=0)
    goles = models.CharField(max_length=10)
    diferencia = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)

    def __str__(self):
        return self.equipo


class Goleador(models.Model):

    jugador = models.CharField(max_length=60)
    goles = models.IntegerField(default=0)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.jugador


class Tarjeta(models.Model):
    jugador = models.CharField(max_length=60)
    amarillas = models.IntegerField(default=0)
    rojas = models.IntegerField(default=0)
    suspendido = models.IntegerField(default=0)

    def __str__(self):
        return self.jugador
