from django.contrib import admin
from .models import Posicion, Goleador, Tarjeta
# Register your models here.

class PosicionAdmin(admin.ModelAdmin):
    list_display = ('posicion','equipo')
    ordering = ['posicion']

admin.site.register(Posicion, PosicionAdmin)
admin.site.register(Goleador)
admin.site.register(Tarjeta)