from import_export import resources
from .models import Peliculas


class PeliculasResource(resources.ModelResource):
    class Meta:
        model = Peliculas
