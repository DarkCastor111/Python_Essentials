from django.db import models

# Create your models here.
class Proyecto(models.Model):
    titulo = models.CharField()
    descripcion = models.TextField()
    imagen = models.ImageField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
