from django.db import models

# Create your models here.

class Jugador(models.Model):
	nombre_completo = models.CharField(max_length=120, blank=True)
	nombre_abreviado = models.CharField(max_length=120, blank=True)
	foto = models.ImageField(blank=True)
	numero = models.IntegerField(default=00)
	posicion = models.CharField(max_length=60)
	fecha_nacimiemto = models.CharField(max_length=120, blank=True)
	peso = models.CharField(max_length=30, blank=True)
	altura = models.CharField(max_length=60, blank=True)
	perfil = models.TextField()

	def __str__(self):
		return self.nombre_abreviado

class Cuerpo_tecnico(models.Model):
	nombre = models.CharField(max_length=120, blank=True)
	puesto = models.CharField(max_length=120, blank=True)
	foto = models.ImageField(blank=True)
	
	def __str__(self):
		return self.nombre

class Directiva(models.Model):
	nombre = models.CharField(max_length=120, blank=True)
	puesto = models.CharField(max_length=120, blank=True)
	foto = models.ImageField(blank=True)
	
	def __str__(self):
		return self.nombre
