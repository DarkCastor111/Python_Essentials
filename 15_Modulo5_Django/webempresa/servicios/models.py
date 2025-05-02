from django.db import models

# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(verbose_name = "Nom")
    subtitulo = models.CharField(verbose_name = "Sous-Titre")
    descripcion = models.TextField(verbose_name = "Description")
    imagen = models.ImageField(verbose_name = "Image", upload_to="servicios")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Date création")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name = "Date modification")

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["-fecha_actualizacion"]

    def __str__(self):
        return self.titulo