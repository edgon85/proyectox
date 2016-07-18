from rest_framework import serializers
from .models import Jugador, Cuerpo_tecnico, Directiva

class JugadorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Jugador
		fields = ("__all__")


class Cuerpo_tecnicoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cuerpo_tecnico
		fields = ("__all__")

class DirectivaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Directiva
		fields = ("__all__")