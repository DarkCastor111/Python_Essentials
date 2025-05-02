from django.contrib import admin
from .models import Servicio

# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_actualizacion','fecha_creacion')

admin.site.register(Servicio, ServicioAdmin)
