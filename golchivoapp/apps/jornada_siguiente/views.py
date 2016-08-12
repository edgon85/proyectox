from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
from .models import Jornada, Alineacion, Directo, Cronica, Resultado
from apps.jornada_anterior.forms import JorndaForm
from rest_framework import viewsets
from .serializers import JornadaSerializer, AlineacionSerializer, DirectoSerializer, CronicaSerializer, ResultadoSerializer


def jornada_list(request):  # lista de jornadas
	queryset = Jornada.objects.all()
	context = {
		'template_title': 'Lista de jornadas',
		'object_list': queryset,
	}
	return render(request, 'jornadas/jornada_list_siguiente.html', context)


def jornada_update(request, id=None):
	instance = get_object_or_404(Jornada, id=id)
	formjsig = JorndaForm(request.POST or None, request.FILES or None, instance=instance)
	if formjsig.is_valid():
		instance = formjsig.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_siguiente:list")

	context = {
		"template_title": 'Actualizar ' + instance.titulo,
		"instance": instance,
		"btn_name": "Editar",
		"formjact": formjsig
	}
	return render(request, 'jornadas/jornada_create.html', context)



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
