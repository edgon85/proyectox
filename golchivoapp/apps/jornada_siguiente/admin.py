from django.contrib import admin

from apps.jornada_siguiente import models
# Register your models here.

admin.site.register(models.Jornada)
admin.site.register(models.Alineacion)
admin.site.register(models.Directo)
admin.site.register(models.Cronica)
admin.site.register(models.Resultado)