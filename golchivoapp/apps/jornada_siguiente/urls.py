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

urlpatterns = [
	#Jornadas
    url(r'^$', login_required(views.jornada_list), name="list"),
    url(r'^(?P<id>\d+)/edit/$',login_required(views.jornada_update), name='jornada_update'),
    #api
    url(r'^', include(router.urls)),

 #    #Alineaciones

 #    #api
 #    url(r'^alienacion/', include(router.urls)),

 #    #Directo

	# #api
 #    url(r'^directo/', include(router.urls)),    

 #    #Cronica

	# #api
 #    url(r'^cronica/', include(router.urls)),

 #    #Resultados

 #    #api
 #    url(r'^resultados/', include(router.urls)),

]