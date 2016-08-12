from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posicionesApi',views.PosicionViewset)
router.register(r'goleadoresApi',views.GoleadorViewset)
router.register(r'tarjetaApi',views.TarjetaViewset)

urlpatterns = [
	#api posiciones
	url(r'^posiciones/', include(router. urls)),

    url(r'^$', login_required(views.Position_list), name="list"),
    url(r'^posicion/(?P<id>\d+)/edit/$',login_required(views.Position_update), name='pos_update'),

	
	#api goleadores
	url(r'^goleadores/', include(router. urls)),
    url(r'^goleador/$', login_required(views.Goldeador_list), name="gol_list"),
    url(r'^goleador/create/$', login_required(views.goleador_create), name="gol_create"),
    url(r'^goleador/(?P<id>\d+)/edit/$',login_required(views.goleador_update), name='gol_update'),

	#api tarjetas
	url(r'^tarjetas/', include(router. urls)),
    url(r'^tarjeta/$', login_required(views.tarjetas_list), name="tarj_list"),
    url(r'^tarjeta/create/$', login_required(views.tarjeta_create), name="tarj_create"),
    url(r'^tarjeta/(?P<id>\d+)/edit/$',login_required(views.tajeta_update), name='tarj_update'),

]
