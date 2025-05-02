from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "core/index.html")

def historia(request):
    return render(request, "core/about.html")

def servicios(request):
    return render(request, "core/services.html")

def visitanos(request):
    return render(request, "core/store.html")

def contacto(request):
    return render(request, "core/contact.html")

def blog(request):
    return render(request, "core/blog.html")

def ejemplo(request):
    return render(request, "core/sample.html")

