from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="nm_inicio"),
    path('about/', views.historia, name="nm_historia"),
    path('store/', views.visitanos, name="nm_visitanos"),


]
