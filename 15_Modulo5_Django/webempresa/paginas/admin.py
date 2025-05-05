from django.contrib import admin
from .models import Pagina

# Register your models here.
class PaginaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    list_display = ('titulo', 'orden')
    
admin.site.register(Pagina, PaginaAdmin)

