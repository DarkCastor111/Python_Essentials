from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "core/index.html")

def historia(request):
    return render(request, "core/about.html")

def visitanos(request):
    return render(request, "core/store.html")



