from django.shortcuts import render, get_object_or_404
from .models import Entrada, Categoria

# Create your views here.
def blog(request):
    todas_las_entradas = Entrada.objects.all()
    return render(request, "blog/blog.html", {'ntrds': todas_las_entradas})

def categoria(request, cat_id):
    categoria_por_id = get_object_or_404(Categoria, id=cat_id)
    entradas_por_categoria = Entrada.objects.filter(categorias=categoria_por_id)
    return render(request, "blog/blog.html", {'ntrds': entradas_por_categoria})

    '''
    categoria_por_id = get_object_or_404(Categoria, id=cat_id)
    return render(request, "blog/cat.html", {'ctg': categoria_por_id})
    '''
    
