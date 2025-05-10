from django.contrib import admin
from .models import Enlace

# Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')

    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name="Personal").exists():
            return ('fecha_creacion', 'fecha_actualizacion', 'clave', 'nombre')
        else:
            return ('fecha_creacion', 'fecha_actualizacion')
    
admin.site.register(Enlace, EnlaceAdmin)

