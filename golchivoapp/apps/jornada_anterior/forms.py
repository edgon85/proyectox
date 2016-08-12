from django import forms
from .models import Jornada, Directo, Cronica, Resultado
from apps.jornada_actual.models import Alineaciones

class JorndaForm(forms.ModelForm):
	class Meta:
		model = Jornada
		fields = [
			"titulo", "fecha", "horario", "estadio", 
			"nom_local","logo_local", "nom_visita",
            "logo_visita","marcador","estado","num_tab"
		]
		labels = {
			"titulo":"Titulo",
			"fecha":"Fecha de jornada",
			"horario":"Horario de jornada",
			"estadio":"Estadio",
			"nom_local":"Nombre equipo local",
            "logo_local":"Logo Local",
			"nom_visita":"Nombre equipo visita",
            "logo_visita": "Logo visita",
			"marcador":"Marcador del Juego",
			"estado":"Estado del juego",
            "num_tab": "Num de tab",
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
            "num_tab": forms.TextInput(attrs={'class': 'form-control'}),
		}

class AlineacionForm(forms.ModelForm):
	class Meta:
		model = Alineaciones
		fields = [
			"nombreJL1",
			"numeroJL1",
			"nombreJV1",
			"numeroJV1",

            "nombreJL2",
            "numeroJL2",
            "nombreJV2",
            "numeroJV2",

            "nombreJL3",
            "numeroJL3",
            "nombreJV3",
            "numeroJV3",

            "nombreJL4",
            "numeroJL4",
            "nombreJV4",
            "numeroJV4",

            "nombreJL5",
            "numeroJL5",
            "nombreJV5",
            "numeroJV5",

            "nombreJL6",
            "numeroJL6",
            "nombreJV6",
            "numeroJV6",

            "nombreJL7",
            "numeroJL7",
            "nombreJV7",
            "numeroJV7",

            "nombreJL8",
            "numeroJL8",
            "nombreJV8",
            "numeroJV8",

            "nombreJL9",
            "numeroJL9",
            "nombreJV9",
            "numeroJV9",

            "nombreJL10",
            "numeroJL10",
            "nombreJV10",
            "numeroJV10",

            "nombreJL11",
            "numeroJL11",
            "nombreJV11",
            "numeroJV11",

            "nombreDtL",
            "nombreDtV",
		]
		labels = {
			"nombreJL1":"Nombre",
			"numeroJL1":"No.",
			"nombreJV1":"Nombre",
			"numeroJV1":"No.",

            "nombreJL2": "Nombre",
            "numeroJL2": "No.",
            "nombreJV2": "Nombre",
            "numeroJV2": "No.",

            "nombreJL3": "Nombre",
            "numeroJL3": "No.",
            "nombreJV3": "Nombre",
            "numeroJV3": "No.",

            "nombreJL4": "Nombre",
            "numeroJL4": "No.",
            "nombreJV4": "Nombre",
            "numeroJV4": "No.",

            "nombreJL5": "Nombre",
            "numeroJL5": "No.",
            "nombreJV5": "Nombre",
            "numeroJV5": "No.",

            "nombreJL6": "Nombre",
            "numeroJL6": "No.",
            "nombreJV6": "Nombre",
            "numeroJV6": "No.",

            "nombreJL7": "Nombre",
            "numeroJL7": "No.",
            "nombreJV7": "Nombre",
            "numeroJV7": "No.",

            "nombreJL8": "Nombre",
            "numeroJL8": "No.",
            "nombreJV8": "Nombre",
            "numeroJV8": "No.",

            "nombreJL9": "Nombre",
            "numeroJL9": "No.",
            "nombreJV9": "Nombre",
            "numeroJV9": "No.",

            "nombreJL10": "Nombre",
            "numeroJL10": "No.",
            "nombreJV10": "Nombre",
            "numeroJV10": "No.",

            "nombreJL11": "Nombre",
            "numeroJL11": "No.",
            "nombreJV11": "Nombre",
            "numeroJV11": "No.",

            "nombreDtL": "Nombre",
            "nombreDtV": "Nombre",
		}
		widgets = {
			"nombreJL1":forms.TextInput(attrs={'class':'form-control'}),
			"numeroJL1":forms.TextInput(attrs={'class':'form-control'}),
			"nombreJV1":forms.TextInput(attrs={'class':'form-control'}),
			"numeroJV1":forms.TextInput(attrs={'class':'form-control'}),

            "nombreJL2": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL2": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV2": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV2": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL3": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL3": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV3": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV3": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL4": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL4": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV4": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV4": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL5": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL5": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV5": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV5": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL6": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL6": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV6": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV6": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL7": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL7": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV7": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV7": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL8": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL8": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV8": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV8": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL9": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL9": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV9": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV9": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL10": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL10": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV10": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV10": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreJL11": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJL11": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreJV11": forms.TextInput(attrs={'class': 'form-control'}),
            "numeroJV11": forms.TextInput(attrs={'class': 'form-control'}),

            "nombreDtL": forms.TextInput(attrs={'class': 'form-control'}),
            "nombreDtV": forms.TextInput(attrs={'class': 'form-control'}),
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




