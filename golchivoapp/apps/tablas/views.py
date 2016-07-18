from django.shortcuts import render
from .models import Posicion, Goleador, Tarjeta

from rest_framework import viewsets
from .serializers import PosicionSerializer, GoleadorSerializer, TarjetaSerializer
# Create your views here.


#------------ API POSICIONES-----------------------------------------
class AlineacionViewset(viewsets.ModelViewSet):
	queryset = Posicion.objects.all()
	serializer_class = PosicionSerializer


#------------ API GOLEADOR-----------------------------------------
class GoleadorViewset(viewsets.ModelViewSet):
	queryset = Goleador.objects.all()
	serializer_class = GoleadorSerializer

#------------ API TARJETAS-----------------------------------------
class TarjetaViewset(viewsets.ModelViewSet):
	queryset = Tarjeta.objects.all()
	serializer_class = TarjetaSerializer
