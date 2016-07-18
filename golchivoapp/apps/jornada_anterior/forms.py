from django import forms
from .models import Jornada, Alineacion, Directo, Cronica, Resultado

class JorndaForm(forms.ModelForm):
	class Meta:
		model = Jornada
		fields = [
			"titulo", "fecha", "horario", "estadio", 
			"nom_local", "nom_visita","marcador","estado",
		]
		labels = {
			"titulo":"Titulo",
			"fecha":"Fecha de jornada",
			"horario":"Horario de jornada",
			"estadio":"Estadio",
			"nom_local":"Nombre equipo local",
			"nom_visita":"Nombre equipo visita",
			"marcador":"Marcador del Juego",
			"estado":"Estado del juego",
		}
		widgets = {
			"titulo":forms.TextInput(attrs={'class':'form-control'}),
			"fecha":forms.TextInput(attrs={'class':'form-control'}),
			"horario":forms.TextInput(attrs={'class':'form-control'}),
			"estadio":forms.TextInput(attrs={'class':'form-control'}),
			"nom_local":forms.TextInput(attrs={'class':'form-control'}),
			"nom_visita":forms.TextInput(attrs={'class':'form-control'}),
			"marcador":forms.TextInput(attrs={'class':'form-control'}),
			"estado":forms.TextInput(attrs={'class':'form-control'}),
		}

class AlineacionForm(forms.ModelForm):
	class Meta:
		model = Alineacion
		fields = [
			"nombre_jugador_local","numero_jugador_local",
			"nombre_jugador_visita","numero_jugador_visita"
		]
		labels = {
			"nombre_jugador_local":"Nombre",
			"numero_jugador_local":"No.",
			"nombre_jugador_visita":"Nombre",
			"numero_jugador_visita":"No.",	
		}
		widgets = {
			"nombre_jugador_local":forms.TextInput(attrs={'class':'form-control'}),
			"numero_jugador_local":forms.TextInput(attrs={'class':'form-control'}),
			"nombre_jugador_visita":forms.TextInput(attrs={'class':'form-control'}),
			"numero_jugador_visita":forms.TextInput(attrs={'class':'form-control'}),	
		}

class DirectoForm(forms.ModelForm):
	class Meta:
		model = Directo
		fields = [
			"minuto", "comentario"
		]
		labels = {
			"minuto":"Minuto",
			"comentario":"Comentario",
		}
		widgets = {
			"minuto":forms.TextInput(attrs={'class':'form-control'}),
			"comentario":forms.Textarea(attrs={'class':'form-control'}),
		}


class CronicaForm(forms.ModelForm):
	class Meta:
		model = Cronica
		fields = [
			"titulo", "cronica"
		]
		labels = {
			"titulo":"Titulo de la cronica",
			"cronica":"Comentario",
		}
		widgets = {
			"titulo":forms.TextInput(attrs={'class':'form-control'}),
			"cronica":forms.Textarea(attrs={'class':'form-control'}),
		}


class ResultadoForm(forms.ModelForm):
	class Meta:
		model = Resultado
		fields = [
			"equipo_uno","resultado_uno",
			"equipo_dos","resultado_dos"
		]
		labels = {
			"equipo_uno":"Nombre de equipo",
			"resultado_uno":"Resultado",
			"equipo_dos":"Nombre de equipo",
			"resultado_dos":"Resultado",	
		}
		widgets = {
			"equipo_uno":forms.TextInput(attrs={'class':'form-control'}),
			"resultado_uno":forms.TextInput(attrs={'class':'form-control'}),
			"equipo_dos":forms.TextInput(attrs={'class':'form-control'}),
			"resultado_dos":forms.TextInput(attrs={'class':'form-control'}),	
		}




