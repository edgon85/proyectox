from django.shortcuts import render, redirect, get_object_or_404
from .models import Jornada, Alineacion, Directo, Cronica, Resultado, Alineaciones
from apps.jornada_anterior.forms import JorndaForm, AlineacionForm, DirectoForm, CronicaForm, ResultadoForm

from rest_framework import viewsets
from .serializers import JornadaSerializer, AlineacionSerializer, DirectoSerializer, CronicaSerializer, \
    ResultadoSerializer, AlineacionesSerializer


# Create your views here.


def jornada_list(request):  # lista de jornadas
	queryset = Jornada.objects.all()
	context = {
		'template_title': 'Lista de jornadas',
		'object_list': queryset,
	}
	return render(request, 'jornadas/jornada_list_actual.html', context)


# -------------------JORNADA CREATE------------------------------------------------------------------


def jornada_create(request):
	formjact = JorndaForm(request.POST or None)
	if formjact.is_valid():
		instance = formjact.save(request.FILES or None, commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_actual:list")

	context = {
		"template_title": 'Nueva Jornada',
		"btn_name": "Crear",
		'formjact': formjact
	}
	return render(request, 'jornadas/jornada_create.html', context)


# -------------------JORNADA UPDATE------------------------------------------------------------------
def jornada_update(request, id=None):
	instance = get_object_or_404(Jornada, id=id)
	formjact = JorndaForm(request.POST or None, request.FILES or None, instance=instance)
	if formjact.is_valid():
		instance = formjact.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_actual:list")

	context = {
		"template_title": 'Actualizar ' + instance.titulo,
		"instance": instance,
		"btn_name": "Editar",
		"formjact": formjact
	}
	return render(request, 'jornadas/jornada_create.html', context)


# -------------------ALINEACION LIST------------------------------------------------------------------

def alineacion_list(request):  # lista de alineaciones
	queryset = Alineaciones.objects.all()
	context = {
		'template_title': 'Lista de alineaciones',
		'object_list': queryset,
	}
	return render(request, 'alineaciones/alineacion_list.html', context)


# -------------------ALINEACION CREATE------------------------------------------------------------------
def alinecion_create(request):
	form = AlineacionForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_actual:alin_list_act")

	context = {
		"template_title": 'Agregar Jugadores',
		"btn_name": "Crear",
		'form': form
	}
	return render(request, 'alineaciones/alineacion_create.html', context)


# -------------------ALINEACION UPDATE------------------------------------------------------------------
def alineacion_update(request, id=None):
	instance = get_object_or_404(Alineaciones, id=id)
	form = AlineacionForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_actual:alin_list_act")

	context = {
		"template_title": 'Actualizar ' + instance.titulo,
		"instance": instance,
		"btn_name": "Editar",
		"form": form
	}
	return render(request, 'alineaciones/alineacion_create.html', context)

#-------------------ALINEACION DELETE------------------------------------------------------------------
def alineacion_delete(request, id= None):
	instance = get_object_or_404(Alineaciones, id=id)
	instance.delete()
	# messages.success(request, "Jornada Eliminada")

	return redirect("jornada_actual:alin_list_act")


#-------------------CRONICA LIST------------------------------------------------------------------

def cronica_list(request): #lista de alineaciones
	queryset = Cronica.objects.all()
	context = {
		'template_title': 'Cronica del partido',
		'object_list':queryset,
	}
	return render(request,'cronicas/cronica_list_actual.html', context)

#-------------------CRONICA UPDATE------------------------------------------------------------------
def cronica_update(request, id=None):
	instance = get_object_or_404(Cronica, id=id)
	form = CronicaForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_actual:cronica_list")

	context = {
		"template_title":'Actualizar ' + instance.titulo,
		"instance":instance,
		"btn_name":"Editar",
		"form":form
	}
	return render(request,'cronicas/cronica_create.html', context)



def resultado_list(request): #lista de alineaciones
	queryset = Resultado.objects.all()
	context = {
		'template_title': 'Resultados',
		'object_list':queryset,
	}
	return render(request,'resultados/resultado_list_actual.html', context)

#-------------------RESULTADOS UPDATE------------------------------------------------------------------
def resultado_update(request, id=None):
	instance = get_object_or_404(Resultado, id=id)
	form = ResultadoForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_actual:result_list")

	context = {
		"template_title":'Actualizar ' + instance.titulo,
		"instance":instance,
		"btn_name":"Editar",
		"form":form
	}
	return render(request,'resultados/resultado_create.html', context)



# -----------------------REST FRAMEWORK-------------------------------------------------------------------------------------------------------------------

# ------------ API JORNADA-----------------------------------------
class JornadaViewSet(viewsets.ModelViewSet):
	queryset = Jornada.objects.all()
	serializer_class = JornadaSerializer


# ------------ API ALINEACION-----------------------------------------
class AlineacionViewSet(viewsets.ModelViewSet):
	queryset = Alineacion.objects.all()
	serializer_class = AlineacionSerializer


# ------------ API DIRECTO-----------------------------------------
class DirectoViewSet(viewsets.ModelViewSet):
	queryset = Directo.objects.all().order_by('-id')
	serializer_class = DirectoSerializer


# ------------ API CRONICA-----------------------------------------
class CronicaViewSet(viewsets.ModelViewSet):
	queryset = Cronica.objects.all()
	serializer_class = CronicaSerializer


# ------------ API RESULTADO-----------------------------------------
class ResultadoViewSet(viewsets.ModelViewSet):
	queryset = Resultado.objects.all()
	serializer_class = ResultadoSerializer


class AlineacionesViewSet(viewsets.ModelViewSet):
	queryset = Alineaciones.objects.all()
	serializer_class = AlineacionesSerializer
