from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="nm_blog"),
    path('category/<int:cat_id>/', views.categoria, name="nm_blogcategoria" )

]