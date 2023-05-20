import imp
from django.urls import path
from . import views

app_name = 'peliculas_app'

urlpatterns = [
    path('', views.ListAllProducts.as_view(), name="home"),
    path('nombre/', views.SordMoviesTitle.as_view(), name="nombre"),
    path('nombreOriginal/', views.SordMoviesOriginalTitle.as_view(),
         name="nombreOriginal"),
    path('fecha/', views.SordMoviesDate.as_view(), name="fecha"),
    path('pelicula/<pk>', views.PeliculaView.as_view(), name="pelicula"),
]
