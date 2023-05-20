from django.contrib import admin
from .models import Peliculas
from import_export.admin import ImportExportModelAdmin
from .resources import PeliculasResource

# Register your models here.


class PeliculasAdmin(ImportExportModelAdmin):
    resourse_class = PeliculasResource
    list_display = ('titulo', 'titulo_original',
                    'url_imagen', 'fecha_estreno', 'sinopsis')


admin.site.register(Peliculas, PeliculasAdmin)
