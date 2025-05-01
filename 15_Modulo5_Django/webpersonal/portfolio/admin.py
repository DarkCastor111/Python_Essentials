from django.contrib import admin
from portfolio.models import Proyecto

# Register your models here.
class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')





admin.site.register(Proyecto, ProyectoAdmin)
