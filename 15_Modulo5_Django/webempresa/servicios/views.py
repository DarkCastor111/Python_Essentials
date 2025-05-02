from django.shortcuts import render
from servicios.models import Servicio

# Create your views here.
def servicios(request):
    todos_los_servicios = Servicio.objects.all()
    return render(request, "servicios/services.html", {'srvcs':todos_los_servicios})


