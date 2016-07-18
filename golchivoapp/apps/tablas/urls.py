from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posicionesApi',views.AlineacionViewset)
router.register(r'goleadoresApi',views.GoleadorViewset)
router.register(r'tarjetaApi',views.TarjetaViewset)

urlpatterns = [
	#api posiciones
	url(r'^posiciones/', include(router. urls)),
	
	#api goleadores
	url(r'^goleadores/', include(router. urls)),

	#api tarjetas
	url(r'^tarjetas/', include(router. urls)),
]
