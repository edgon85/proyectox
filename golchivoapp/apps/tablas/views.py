from django.shortcuts import render, redirect, get_object_or_404
from .models import Posicion, Goleador, Tarjeta
from .forms import PosicionForm, GoleadorForm, TarjetaForm


from rest_framework import viewsets
from .serializers import PosicionSerializer, GoleadorSerializer, TarjetaSerializer
# Create your views here.


def Position_list(request):  # lista de jornadas
	queryset = Posicion.objects.all().order_by("posicion")
	context = {
		'template_title': 'Tabla de Posiciones',
		'object_list': queryset,
	}
	return render(request, 'tablas/position_list.html', context)


def Position_update(request, id=None):
	instance = get_object_or_404(Posicion, id=id)
	formjact = PosicionForm(request.POST or None, instance=instance)
	if formjact.is_valid():
		instance = formjact.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("tablas:list")

	context = {
		"template_title": 'Actualizar ' + instance.equipo,
		"instance": instance,
		"btn_name": "Editar",
		"form": formjact
	}
	return render(request, 'tablas/tabla_create.html', context)


def Goldeador_list(request):
    queryset = Goleador.objects.all().order_by("-goles")

    context = {
        'template_title': 'Tabla de Goleadores',
        'object_list': queryset
    }
    return render(request, 'tablas/goleador_list.html', context)


def goleador_create(request):
	form = GoleadorForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("tablas:gol_list")

	context = {
		"template_title": 'Nuevo goleador',
		"btn_name": "Crear",
		'form': form
	}
	return render(request, 'tablas/goleador_create.html', context)


def goleador_update(request, id=None):
	instance = get_object_or_404(Goleador, id=id)
	form = GoleadorForm(request.POST or None,request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("tablas:gol_list")

	context = {
		"template_title": 'Actualizar ' + instance.jugador,
		"instance": instance,
		"btn_name": "Editar",
		"form": form
	}
	return render(request, 'tablas/goleador_create.html', context)




def tarjetas_list(request):  # lista de jornadas
	queryset = Tarjeta.objects.all().order_by("-amarillas")
	context = {
		'template_title': 'Tabla de Tarjetas',
		'object_list': queryset,
	}
	return render(request, 'tablas/tarjeta_list.html', context)



def tarjeta_create(request):
	form = TarjetaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("tablas:tarj_list")

	context = {
		"template_title": 'Crear nueva tarjeta',
		"btn_name": "Crear",
		'form': form
	}
	return render(request, 'tablas/tarjeta_create.html', context)


def tajeta_update(request, id=None):
	instance = get_object_or_404(Tarjeta, id=id)
	form = TarjetaForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("tablas:tarj_list")

	context = {
		"template_title": 'Actualizar ' + instance.jugador,
		"instance": instance,
		"btn_name": "Editar",
		"form": form
	}
	return render(request, 'tablas/tarjeta_create.html', context)



#------------ API POSICIONES-----------------------------------------
class PosicionViewset(viewsets.ModelViewSet):
	queryset = Posicion.objects.all().order_by("posicion")
	serializer_class = PosicionSerializer


#------------ API GOLEADOR-----------------------------------------
class GoleadorViewset(viewsets.ModelViewSet):
	queryset = Goleador.objects.all().order_by("-goles")
	serializer_class = GoleadorSerializer

#------------ API TARJETAS-----------------------------------------
class TarjetaViewset(viewsets.ModelViewSet):
	queryset = Tarjeta.objects.all().order_by("-amarillas")
	serializer_class = TarjetaSerializer
