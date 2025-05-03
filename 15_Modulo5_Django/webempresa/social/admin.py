from django.contrib import admin
from .models import Enlace

# Register your models here.
class EnlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
admin.site.register(Enlace, EnlaceAdmin)

