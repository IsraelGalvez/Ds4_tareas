from django.views.generic import (
    ListView, DetailView
)

from dateutil.parser import parse
from .models import Peliculas
from apps.Peliculas.models import Peliculas

# Create your views here.


class ListAllProducts(ListView):
    template_name = 'peliculas/main.html'
    model = Peliculas


class SordMoviesTitle(ListView):
    template_name = 'peliculas/nombre.html'
    model = Peliculas
    context_object_name = 'peliculas'
    ordering = ['titulo']


class SordMoviesOriginalTitle(ListView):
    template_name = 'peliculas/nombreOriginal.html'
    model = Peliculas
    context_object_name = 'peliculas'
    ordering = ['titulo_original']


class SordMoviesDate(ListView):
    template_name = 'peliculas/fecha.html'
    model = Peliculas
    context_object_name = 'peliculas'
    ordering = ['fecha_estreno']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['peliculas'] = self.format_dates(context['peliculas'])
        return context

    def format_dates(self, peliculas):
        for pelicula in peliculas:
            fecha_estreno = pelicula.fecha_estreno
            if isinstance(fecha_estreno, str):
                try:
                    date_obj = parse(fecha_estreno)
                    formatted_date = date_obj.strftime('%Y-%m-%d')
                    pelicula.fecha_estreno = formatted_date
                except ValueError:
                    # La fecha no es válida, se formatea a una fecha válida
                    formatted_date = 'Fecha inválida'
                    pelicula.fecha_estreno = formatted_date
        return peliculas


class PeliculaView(DetailView):
    """ Trae la informacion de un producto con el id """
    model = Peliculas
    template_name = 'peliculas/pelicula.html'
    context_object_name = 'pelicula'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context["object_list"] = Peliculas.objects.filter(
            id=pk
        )

        return context
