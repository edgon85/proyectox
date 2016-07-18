from django.shortcuts import render, redirect, get_object_or_404
from .models import Jornada, Alineacion, Directo, Cronica, Resultado
from .forms import JorndaForm, AlineacionForm, DirectoForm, CronicaForm, ResultadoForm

from rest_framework import viewsets
from .serializers import JornadaSerializer, AlineacionSerializer, DirectoSerializer, CronicaSerializer, ResultadoSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

def home(request):
	return render(request, 'base/home.html',{})
#-------------------JORNADA LIST------------------------------------------------------------------

def jornada_list(request): #lista de jornadas
	queryset = Jornada.objects.all()
	context = {
		'template_title': 'Lista de jornadas',
		'object_list':queryset,
	}
	return render(request,'jornadas/jornada_list.html', context)

#-------------------JORNADA CREATE------------------------------------------------------------------
def jornada_create(request):
	form = JorndaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:list")

	context = {
		"template_title":'Nueva Jornada',
		"btn_name":"Crear",
		'form':form
	}
	return render(request,'jornadas/jornada_create.html', context)


#-------------------JORNADA RETRIVE------------------------------------------------------------------
def jornada_detail(request, id=None): #retrive
	instance = get_object_or_404(Jornada, id=id)

	context = {
		"template_title":"Detalle de Jornada",
		"instance":instance
	}
	return render(request,'jornadas/jornada_detail.html', context)


# #-------------------JORNADA UPDATE------------------------------------------------------------------
def jornada_update(request, id=None):
	instance = get_object_or_404(Jornada, id=id)
	form = JorndaForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:list")

	context = {
		"template_title":'Actualizar ' + instance.titulo,
		"instance":instance,
		"btn_name":"Editar",
		"form":form
	}
	return render(request,'jornadas/jornada_create.html', context)



# #-------------------JORNADA DELETE------------------------------------------------------------------
def jornada_delete(request, id= None):
	instance = get_object_or_404(Jornada, id=id)
	instance.delete()
	# messages.success(request, "Jornada Eliminada")

	return redirect("jornada_uno:list")

# ------------------------------------------------------------------------------------------------------------------------------------------


# #-------------------ALINEACION LIST------------------------------------------------------------------

def alineacion_list(request): #lista de alineaciones
	queryset = Alineacion.objects.all()
	context = {
		'template_title': 'Lista de alineaciones',
		'object_list_alin':queryset,
	}
	return render(request,'alineaciones/alineacion_list.html', context)

#-------------------ALINEACION CREATE------------------------------------------------------------------
def alinecion_create(request):
	form = AlineacionForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:alin_list")

	context = {
		"template_title":'Agregar Jugadores',
		"btn_name":"Crear",
		'form':form
	}
	return render(request,'alineaciones/alineacion_create.html', context)


#-------------------ALINEACION RETRIVE------------------------------------------------------------------
def alineacion_detail(request, id=None): #retrive
	instance = get_object_or_404(Alineacion, id=id)

	context = {
		"template_title":"Detalle de Jugadores",
		"instance":instance
	}
	return render(request,'alineaciones/alineacion_detail.html', context)

#-------------------ALINEACION UPDATE------------------------------------------------------------------
def alineacion_update(request, id=None):
	instance = get_object_or_404(Alineacion, id=id)
	form = AlineacionForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:alin_list")

	context = {
		"template_title":'Actualizar ' + instance.titulo,
		"instance":instance,
		"btn_name":"Editar",
		"form":form
	}
	return render(request,'alineaciones/alineacion_create.html', context)



# #-------------------ALINEACION DELETE------------------------------------------------------------------
def alineacion_delete(request, id= None):
	instance = get_object_or_404(Alineacion, id=id)
	instance.delete()
	# messages.success(request, "Jornada Eliminada")

	return redirect("jornada_uno:alin_list")

# ------------------------------------------------------------------------------------------------------------------------------------------


#-------------------DIRECTO LIST------------------------------------------------------------------

def directo_list(request): #lista de alineaciones
	queryset = Directo.objects.all()
	context = {
		'template_title': 'Listado en directo',
		'object_list':queryset,
	}
	return render(request,'directo/directo_list.html', context)

#-------------------DIRECTO CREATE------------------------------------------------------------------
def directo_create(request):
	form = DirectoForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:direct_list")

	context = {
		"template_title":'Agregar Comentario',
		"btn_name":"Crear",
		'form':form
	}
	return render(request,'directo/directo_create.html', context)


#-------------------DIRECTO RETRIVE------------------------------------------------------------------
def directo_detail(request, id=None): #retrive
	instance = get_object_or_404(Directo, id=id)

	context = {
		"template_title":"Detalle en directo",
		"instance":instance
	}
	return render(request,'directo/directo_detail.html', context)

#-------------------DIRECTO UPDATE------------------------------------------------------------------
def directo_update(request, id=None):
	instance = get_object_or_404(Directo, id=id)
	form = DirectoForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:direct_list")

	context = {
		"template_title":'Actualizar minuto ' + instance.minuto,
		"instance":instance,
		"btn_name":"Editar",
		"form":form
	}
	return render(request,'directo/directo_create.html', context)



# #-------------------DIRECTO DELETE------------------------------------------------------------------
def directo_delete(request, id= None):
	instance = get_object_or_404(Directo, id=id)
	instance.delete()
	# messages.success(request, "Jornada Eliminada")

	return redirect("jornada_uno:direct_list")

# ------------------------------------------------------------------------------------------------------------------------------------------

#=====>

#-------------------CRONICA LIST------------------------------------------------------------------

def cronica_list(request): #lista de alineaciones
	queryset = Cronica.objects.all()
	context = {
		'template_title': 'Listado cronicas',
		'object_list':queryset,
	}
	return render(request,'cronicas/cronica_list.html', context)

#-------------------CRONICA CREATE------------------------------------------------------------------
def cronica_create(request):
	form = CronicaForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:cronica_list")

	context = {
		"template_title":'Agregar cronica',
		"btn_name":"Crear",
		'form':form
	}
	return render(request,'cronicas/cronica_create.html', context)


#-------------------CRONICA RETRIVE------------------------------------------------------------------
def cronica_detail(request, id=None): #retrive
	instance = get_object_or_404(Cronica, id=id)

	context = {
		"template_title":"Detalle de la cronica",
		"instance":instance
	}
	return render(request,'cronicas/cronica_detail.html', context)

#-------------------CRONICA UPDATE------------------------------------------------------------------
def cronica_update(request, id=None):
	instance = get_object_or_404(Cronica, id=id)
	form = CronicaForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:cronica_list")

	context = {
		"template_title":'Actualizar ' + instance.titulo,
		"instance":instance,
		"btn_name":"Editar",
		"form":form
	}
	return render(request,'cronicas/cronica_create.html', context)



# #-------------------CRONICA DELETE------------------------------------------------------------------
def cronica_delete(request, id= None):
	instance = get_object_or_404(Cronica, id=id)
	instance.delete()
	# messages.success(request, "Jornada Eliminada")

	return redirect("jornada_uno:cronica_list")

# ------------------------------------------------------------------------------------------------------------------------------------------

#=====>

#-------------------RESULTADOS LIST------------------------------------------------------------------

def resultado_list(request): #lista de alineaciones
	queryset = Resultado.objects.all()
	context = {
		'template_title': 'Resultados',
		'object_list':queryset,
	}
	return render(request,'resultados/resultado_list.html', context)

#-------------------RESULTADOS CREATE------------------------------------------------------------------
def resultado_create(request):
	form = ResultadoForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Creado satisfactoriamente")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:result_list")

	context = {
		"template_title":'Agregar resultados',
		"btn_name":"Crear",
		'form':form
	}
	return render(request,'resultados/resultado_create.html', context)


#-------------------RESULTADOS RETRIVE------------------------------------------------------------------
def resultado_detail(request, id=None): #retrive
	instance = get_object_or_404(Resultado, id=id)

	context = {
		"template_title":"Detalle del resultado",
		"instance":instance
	}
	return render(request,'resultados/resultado_detail.html', context)

#-------------------RESULTADOS UPDATE------------------------------------------------------------------
def resultado_update(request, id=None):
	instance = get_object_or_404(Resultado, id=id)
	form = ResultadoForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# messages.success(request, "Jornada guardada")
		# return HttpResponseRedirect(instance.get_absolute_url())
		return redirect("jornada_uno:result_list")

	context = {
		"template_title":'Actualizar ' + instance.titulo,
		"instance":instance,
		"btn_name":"Editar",
		"form":form
	}
	return render(request,'resultados/resultado_create.html', context)



# #-------------------RESULTADOS DELETE------------------------------------------------------------------
def resultado_delete(request, id= None):
	instance = get_object_or_404(Resultado, id=id)
	instance.delete()
	# messages.success(request, "Jornada Eliminada")

	return redirect("jornada_uno:result_list")

# ------------------------------------------------------------------------------------------------------------------------------------------

# -----------------------REST FRAMEWORK-------------------------------------------------------------------------------------------------------------------

#------------ API JORNADA-----------------------------------------
class JornadaViewSet(viewsets.ModelViewSet):
	queryset = Jornada.objects.all()
	serializer_class = JornadaSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)

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


