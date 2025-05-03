from .models import Enlace

def ctx_dict(request):

    ctx = {}
    enlaces = Enlace.objects.all()
    for enlace in enlaces:
        ctx[enlace.clave] = enlace.url
    return ctx