from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(verbose_name = "Nom")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Date création")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name = "Date modification")
    
    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"
        ordering = ["-fecha_actualizacion"]

    def __str__(self):
        return self.nombre
    
class Entrada(models.Model):
    titulo = models.CharField(verbose_name = "Titre")
    contenido = models.TextField(verbose_name = "Contenu")
    fecha_publicacion = models.DateTimeField(verbose_name = "Date Publication", default=now)
    imagen = models.ImageField(verbose_name = "Image", upload_to="blog", null=True, blank=True)
    autor = models.ForeignKey(User, verbose_name="Auteur", on_delete=models.PROTECT, null=True, blank=True)
    categorias = models.ManyToManyField(Categoria, verbose_name="Catégories", related_name="entradas")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Date création")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name = "Date modification")
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ["-fecha_actualizacion"]

    def __str__(self):
        return self.titulo
    