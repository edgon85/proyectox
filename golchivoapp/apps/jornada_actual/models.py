from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.

class Jornada(models.Model):
	titulo = models.CharField(max_length=30, blank=True, default=" ")
	fecha = models.CharField(max_length=30, blank=True)
	horario = models.CharField(max_length=20, blank=True)
	estadio = models.CharField(max_length=50, blank=True)
	nom_local = models.CharField(max_length=100, blank=True)
	logo_local = models.ImageField(blank=True)
	nom_visita = models.CharField(max_length=100, blank=True)
	logo_visita = models.ImageField(blank=True)
	marcador = models.CharField(max_length=15, blank=True, default=" ")
	estado = models.CharField(max_length=15, blank=True, default=" ")
	num_tab = models.IntegerField(default=0, blank=True)

	# alineacion = models.ManyToManyField(Alineacion, null=True, blank=True)

	def __str__(self):
		return self.titulo


class Alineacion(models.Model):
	titulo = models.CharField(max_length=30, blank=True, default="Alineacion")
	nombre_jugador_local = models.CharField(max_length=50, default="-", blank=True)
	numero_jugador_local = models.CharField("No.", max_length=3, default="-", blank=True)
	nombre_jugador_visita = models.CharField(max_length=50, default="-", blank=True)
	numero_jugador_visita = models.CharField("No.", max_length=3, default="-", blank=True)

	# jornada = models.ForeignKey(Jornada, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo


class Directo(models.Model):
	titulo = models.CharField(max_length=30, blank=True, default="En directo")
	minuto = models.CharField(max_length=3, default=" ", blank=True)
	comentario = models.TextField(default=" ", blank=True)

	def __str__(self):
		return self.titulo


class Cronica(models.Model):
	titulo = models.CharField(max_length=200, blank=True, default="Cronica")
	cronica = models.TextField(default=" ", blank=True)

	def __str__(self):
		return self.titulo


class Resultado(models.Model):
	titulo = titulo = models.CharField(max_length=30, blank=True, default="Resultados")
	equipo_uno = models.CharField(max_length=60, blank=True, default=" ")
	resultado_uno = models.CharField(max_length=4, blank=True, default=" ")
	equipo_dos = models.CharField(max_length=60, blank=True, default=" ")
	resultado_dos = models.CharField(max_length=4, blank=True, default=" ")

	def __str__(self):
		return self.titulo


class Alineaciones(models.Model):
	titulo = models.CharField(max_length=30, blank=True, default="Alineacion")

	nombreJL1 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL1 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL2 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL2 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL3 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL3 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL4 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL4 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL5 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL5 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL6 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL6 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL7 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL7 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL8 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL8 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL9 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL9 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL10 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL10 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJL11 = models.CharField(max_length=50, default="-", blank=True)
	numeroJL11 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreDtL = models.CharField(max_length=50, default="-", blank=True)
	numeroDtL = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV1 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV1 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV2 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV2 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV3 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV3 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV4 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV4 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV5 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV5 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV6 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV6 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV7 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV7 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV8 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV8 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV9 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV9 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV10 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV10 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreJV11 = models.CharField(max_length=50, default="-", blank=True)
	numeroJV11 = models.CharField("No.", max_length=3, default="-", blank=True)

	nombreDtV = models.CharField(max_length=50, default="-", blank=True)
	numeroDtV = models.CharField("No.", max_length=3, default="-", blank=True)


