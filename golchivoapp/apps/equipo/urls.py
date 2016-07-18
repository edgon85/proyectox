from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'jugadoresApi',views.JugadorViewset)
router.register(r'Cuerpo_tecnicoApi',views.CuerpoTecnicoViewset)
router.register(r'DirectivaApi',views.DirectivaViewset)

urlpatterns = [
	#api jugadores
	url(r'^jugadores/', include(router. urls)),
	#api cuerpo tecnico
	url(r'^cuerpo_tecnico/', include(router. urls)),
	#api directiva
	url(r'^directiva/', include(router. urls)),
]