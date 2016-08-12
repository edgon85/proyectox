from django import forms
from .models import Posicion, Goleador, Tarjeta

class PosicionForm(forms.ModelForm):
	class Meta:
		model = Posicion
		fields = [
			"posicion", "equipo","partidos","goles","diferencia","puntos"
		]
		# labels = {
		# 	"titulo":"Titulo de la cronica",
		# 	"cronica":"Comentario",
		# }
		# widgets = {
		# 	"titulo":forms.TextInput(attrs={'class':'form-control'}),
		# 	"cronica":forms.Textarea(attrs={'class':'form-control'}),
		# }

class GoleadorForm(forms.ModelForm):
	class Meta:
		model = Goleador
		fields = [
			"jugador","photo", "goles"
		]


class TarjetaForm(forms.ModelForm):
	class Meta:
		model = Tarjeta
		fields = [
			"jugador","amarillas", "rojas", "suspendido"
		]