from django.conf.urls import url, include
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