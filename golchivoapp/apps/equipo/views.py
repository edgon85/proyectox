from django.shortcuts import render
from .models import Jugador, Cuerpo_tecnico, Directiva

from rest_framework import viewsets
from .serializers import JugadorSerializer, Cuerpo_tecnicoSerializer, DirectivaSerializer
# Create your views here.


#------------ API Jugadores-----------------------------------------
class JugadorViewset(viewsets.ModelViewSet):
	queryset = Jugador.objects.all()
	serializer_class = JugadorSerializer

#------------ API Cuerpo tecnico-----------------------------------------
class CuerpoTecnicoViewset(viewsets.ModelViewSet):
	queryset = Cuerpo_tecnico.objects.all()
	serializer_class = Cuerpo_tecnicoSerializer

#------------ API Directiva-----------------------------------------
class DirectivaViewset(viewsets.ModelViewSet):
	queryset = Directiva.objects.all()
	serializer_class = DirectivaSerializer