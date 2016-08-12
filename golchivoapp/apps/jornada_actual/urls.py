from django.conf.urls import url, include
from . import views
from django.contrib.auth.decorators import login_required
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'jornadaApi', views.JornadaViewSet)
router.register(r'alineacionApi', views.AlineacionViewSet)
router.register(r'directoApi', views.DirectoViewSet)
router.register(r'cronicaApi', views.CronicaViewSet)
router.register(r'resultadoApi', views.ResultadoViewSet)
router.register(r'alineacionesApi', views.AlineacionesViewSet)

urlpatterns = [
    # Jornadas
    url(r'^$', login_required(views.jornada_list), name="list"),
    url(r'^create/$', login_required(views.jornada_create), name="jornada_create"),
    #url(r'^(?P<id>\d+)/$',login_required(views.jornada_detail), name='jornada_detail'),
    url(r'^(?P<id>\d+)/edit/$',login_required(views.jornada_update), name='jornada_update'),
    #api
    url(r'^', include(router.urls)),

    #Alineaciones
    url(r'^alineacion/$', login_required(views.alineacion_list), name="alin_list_act"),
    url(r'^alineacion/create/$', login_required(views.alinecion_create), name="alin_create"),
    url(r'^alineacion/(?P<id>\d+)/edit/$',login_required(views.alineacion_update), name='alin_update'),
    url(r'^alineacion/(?P<id>\d+)/delete/$',login_required(views.alineacion_delete), name='alin_delete'),
 #    #api
 #    url(r'^alienacion/', include(router.urls)),

 #    #Directo

	# #api
 #    url(r'^directo/', include(router.urls)),    

 #    #Cronica
    url(r'^cronica/$', login_required(views.cronica_list), name="cronica_list"),
    url(r'^cronica/(?P<id>\d+)/edit/$',login_required(views.cronica_update), name='cronica_update'),
	# #api
 #    url(r'^cronica/', include(router.urls)),

     #    #Resultados
    url(r'^resultados/$', login_required(views.resultado_list), name="result_list"),
    url(r'^resultados/(?P<id>\d+)/edit/$',login_required(views.resultado_update), name='result_update'),
    #url(r'^resultados/(?P<id>\d+)/delete/$',login_required(views.resultado_delete), name='result_delete'),
 #    #api
 #    url(r'^resultados/', include(router.urls)),

]