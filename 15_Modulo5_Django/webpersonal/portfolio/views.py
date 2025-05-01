from django.shortcuts import render
from portfolio.models import Proyecto

# Create your views here.
def portfolio(request):
    proyectos = Proyecto.objects.all()
    return render(request, "portfolio/portfolio.html", {'prcts':proyectos})
