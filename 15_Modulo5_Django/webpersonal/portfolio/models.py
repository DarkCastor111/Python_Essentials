from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField(verbose_name = "Nom")
    descripcion = models.TextField(verbose_name = "Description")
    imagen = models.ImageField(verbose_name = "Image", upload_to="proyectos")
    enlace = models.URLField(null=True, blank=True, verbose_name = "Lien Web")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Date création")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name = "Date modification")

    class Meta:
        verbose_name = "Projet"
        verbose_name_plural = "Projets"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.titulo

