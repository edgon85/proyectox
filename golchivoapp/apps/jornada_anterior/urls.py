from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'jornadaApi', views.JornadaViewSet)
router.register(r'alineacionApi', views.AlineacionViewSet)
router.register(r'directoApi', views.DirectoViewSet)
router.register(r'cronicaApi', views.CronicaViewSet)
router.register(r'resultadoApi', views.ResultadoViewSet)

urlpatterns = [
	#Jornadas
    
    url(r'^$', login_required(views.jornada_list), name="list"),
    url(r'^create/$', login_required(views.jornada_create), name="jornada_create"),
    url(r'^(?P<id>\d+)/$',login_required(views.jornada_detail), name='jornada_detail'),
    url(r'^(?P<id>\d+)/edit/$',login_required(views.jornada_update), name='jornada_update'),
    url(r'^(?P<id>\d+)/delete/$',login_required(views.jornada_delete), name='delete'),
    #api
    url(r'^', include(router.urls)),


    #Alineaciones
    url(r'^alineacion/$', login_required(views.alineacion_list), name="alin_list"),
    url(r'^alineacion/create/$', login_required(views.alinecion_create), name="alin_create"),
    url(r'^alineacion/(?P<id>\d+)/$',login_required(views.alineacion_detail), name='alin_detail'),
    url(r'^alineacion/(?P<id>\d+)/edit/$',login_required(views.alineacion_update), name='alin_update'),
    url(r'^alineacion/(?P<id>\d+)/delete/$',login_required(views.alineacion_delete), name='alin_delete'),
    #api
    #url(r'^alienacion/', include(router.urls)),

    #Directo
    url(r'^directo/$', login_required(views.directo_list), name="direct_list"),
    url(r'^directo/create/$', login_required(views.directo_create), name="direct_create"),
    url(r'^directo/(?P<id>\d+)/$',login_required(views.directo_detail), name='direct_detail'),
    url(r'^directo/(?P<id>\d+)/edit/$',login_required(views.directo_update), name='direct_update'),
    url(r'^directo/(?P<id>\d+)/delete/$',login_required(views.directo_delete), name='direct_delete'),
    #api
    #url(r'^directo/', include(router.urls)),

    #Cronica
    url(r'^cronica/$', login_required(views.cronica_list), name="cronica_list"),
    url(r'^cronica/create/$', login_required(views.cronica_create), name="cronica_create"),
    url(r'^cronica/(?P<id>\d+)/$',login_required(views.cronica_detail), name='cronica_detail'),
    url(r'^cronica/(?P<id>\d+)/edit/$',login_required(views.cronica_update), name='cronica_update'),
    url(r'^cronica/(?P<id>\d+)/delete/$',login_required(views.cronica_delete), name='cronica_delete'),
    #api
    #url(r'^cronica/', include(router.urls)),

    #Resultados
    url(r'^resultados/$', login_required(views.resultado_list), name="result_list"),
    url(r'^resultados/create/$', login_required(views.resultado_create), name="result_create"),
    url(r'^resultados/(?P<id>\d+)/$',login_required(views.resultado_detail), name='result_detail'),
    url(r'^resultados/(?P<id>\d+)/edit/$',login_required(views.resultado_update), name='result_update'),
    url(r'^resultados/(?P<id>\d+)/delete/$',login_required(views.resultado_delete), name='result_delete'),
    #api
    #url(r'^resultados/', include(router.urls)),

]