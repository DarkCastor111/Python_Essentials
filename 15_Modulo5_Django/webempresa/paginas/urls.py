from django.urls import path
from . import views

urlpatterns = [
    path('<int:pg_id>/<slug:pg_slug>', views.pagina, name="nm_pagina"),
]