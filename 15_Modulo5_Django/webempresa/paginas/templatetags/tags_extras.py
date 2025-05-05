from django import template
from paginas.models import Pagina

register = template.Library()

@register.simple_tag
def get_listado_paginas():
    pgs = Pagina.objects.all()
    return pgs