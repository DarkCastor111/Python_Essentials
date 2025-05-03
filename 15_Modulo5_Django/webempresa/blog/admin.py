from django.contrib import admin
from .models import Categoria, Entrada

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_actualizacion','fecha_creacion')

admin.site.register(Categoria, CategoriaAdmin)

class EntradaAdmin(admin.ModelAdmin):
    readonly_fields = ('fecha_actualizacion','fecha_creacion')
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'post_categorias')
    ordering = ('autor', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido', 'autor__username', 'categorias__nombre')
    date_hierarchy = ('fecha_publicacion')
    list_filter = ('autor__username', 'categorias__nombre')

    def post_categorias(self, obj):
        return ", ".join([c.nombre for c in obj.categorias.all().order_by("nombre")])
    post_categorias.short_description = 'Catégories'

admin.site.register(Entrada, EntradaAdmin)
