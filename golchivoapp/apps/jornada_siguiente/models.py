from django.db import models

# Create your models here.

class Jornada(models.Model):
	titulo = models.CharField(max_length=30, blank=True, default=" ")
	fecha = models.CharField(max_length=30, blank=True)
	horario = models.CharField(max_length=20, blank=True)
	estadio = models.CharField(max_length=50, blank=True)
	nom_local = models.CharField(max_length=100, blank=True)
	logo_local = models.ImageField(blank=True)
	nom_visita = models.CharField(max_length=100, blank=True)
	logo_visita= models.ImageField(blank=True)
	marcador = models.CharField(max_length=15, blank=True, default=" ")
	estado = models.CharField(max_length=15,  blank=True, default=" ")
	num_tab = models.IntegerField(default=0, blank=True)
	#alineacion = models.ManyToManyField(Alineacion, null=True, blank=True)

	def __str__(self):
		return self.titulo

class Alineacion(models.Model):
	titulo = models.CharField(max_length=30, blank=True, default="Alineacion")
	nombre_jugador_local = models.CharField(max_length=50, default="-",blank=True)
	numero_jugador_local = models.CharField("No.", max_length=3, default="-",blank=True)
	nombre_jugador_visita = models.CharField(max_length=50, default="-",blank=True)
	numero_jugador_visita = models.CharField("No.",max_length=3, default="-",blank=True)
	# jornada = models.ForeignKey(Jornada, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.titulo



class Directo(models.Model):
	titulo = models.CharField(max_length=30, blank=True, default="En directo")
	minuto = models.CharField(max_length=3, default=" ",blank=True)
	comentario = models.TextField(default=" ",blank=True)

	def __str__(self):
		return self.titulo


class Cronica(models.Model):
	titulo = models.CharField(max_length=200, blank=True, default="Cronica")
	cronica = models.TextField(default=" ",blank=True)

	def __str__(self):
		return self.titulo


class Resultado(models.Model):
	titulo = titulo = models.CharField(max_length=30, blank=True, default="Resultados")
	equipo_uno = models.CharField(max_length=60,blank=True,default=" ")
	resultado_uno = models.CharField(max_length=4,blank=True,default=" ")
	equipo_dos = models.CharField(max_length=60,blank=True,default=" ")
	resultado_dos = models.CharField(max_length=4,blank=True,default=" ")

	def __str__(self):
		return self.titulo
