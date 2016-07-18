from rest_framework import serializers
from .models import Posicion, Goleador, Tarjeta

class PosicionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Posicion
		fields = ("__all__")

class GoleadorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Goleador
		fields = ("__all__")

class TarjetaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Tarjeta
		fields = ("__all__")