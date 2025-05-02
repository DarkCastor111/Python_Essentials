from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    return HttpResponse('<h1> Inicio </h1>')

def historia(request):
    return HttpResponse('<h1> Historia </h1>')

def servicios(request):
    return HttpResponse('<h1> Servicios </h1>')

def visitanos(request):
    return HttpResponse('<h1> Visitanos </h1>')

def contacto(request):
    return HttpResponse('<h1> Contacto </h1>')

def blog(request):
    return HttpResponse('<h1> Blog </h1>')

def ejemplo(request):
    return HttpResponse('<h1> Ejemplo </h1>')

