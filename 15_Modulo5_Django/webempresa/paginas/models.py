from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Pagina(models.Model):
    titulo = models.CharField(verbose_name = "Titre")
    contenido = RichTextField(verbose_name = "Contenu")
    orden = models.SmallIntegerField(verbose_name = "Position", default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Date création")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name = "Date modification")

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        ordering = ["orden", "titulo"]

    def __str__(self):
        return self.titulo