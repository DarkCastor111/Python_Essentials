from django.shortcuts import render, get_object_or_404
from .models import Pagina

# Create your views here.
def pagina(request, pg_id, pg_slug):
    # El pg_slug sirve solo para aparecer en el enlace
    # No sirve en la vista
    pagina_encontrada = get_object_or_404(Pagina, id=pg_id)
    return render(request, 'paginas/sample.html', {'pgn':pagina_encontrada})
