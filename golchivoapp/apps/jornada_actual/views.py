from django.shortcuts import render
from .models import Jornada, Alineacion, Directo, Cronica, Resultado
#from .forms import JorndaForm, AlineacionForm, DirectoForm, CronicaForm, ResultadoForm

from rest_framework import viewsets
from .serializers import JornadaSerializer, AlineacionSerializer, DirectoSerializer, CronicaSerializer, ResultadoSerializer


# Create your views here.

# -----------------------REST FRAMEWORK-------------------------------------------------------------------------------------------------------------------

#------------ API JORNADA-----------------------------------------
class JornadaViewSet(viewsets.ModelViewSet):
	queryset = Jornada.objects.all()
	serializer_class = JornadaSerializer

#------------ API ALINEACION-----------------------------------------
class AlineacionViewSet(viewsets.ModelViewSet):
	queryset = Alineacion.objects.all()
	serializer_class = AlineacionSerializer

#------------ API DIRECTO-----------------------------------------
class DirectoViewSet(viewsets.ModelViewSet):
	queryset = Directo.objects.all().order_by('-id')
	serializer_class = DirectoSerializer

#------------ API CRONICA-----------------------------------------
class CronicaViewSet(viewsets.ModelViewSet):
	queryset = Cronica.objects.all()
	serializer_class = CronicaSerializer

#------------ API RESULTADO-----------------------------------------
class ResultadoViewSet(viewsets.ModelViewSet):
	queryset = Resultado.objects.all()
	serializer_class = ResultadoSerializer
