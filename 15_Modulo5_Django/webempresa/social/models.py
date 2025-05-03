from django.db import models

# Create your models here.
class Enlace(models.Model):
    clave = models.SlugField(verbose_name = "Clé", unique=True)
    nombre = models.CharField(verbose_name = "Réseau Social")
    url = models.URLField(verbose_name = "Lien", null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name = "Date création")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name = "Date modification")

    class Meta:
        verbose_name = "Lien"
        verbose_name_plural = "Liens"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre