from rest_framework import serializers
from .models import Jornada, Alineacion, Directo, Cronica, Resultado


class JornadaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Jornada
		fields = ("__all__")

class AlineacionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Alineacion
		fields = ("__all__")


class DirectoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Directo
		fields = ("__all__")

class CronicaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cronica
		fields = ("__all__")


class ResultadoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Resultado
		fields = ("__all__")