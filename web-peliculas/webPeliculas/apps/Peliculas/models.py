from django.db import models
from datetime import datetime

# Create your models here.


class Peliculas(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    titulo_original = models.CharField('Titulo original', max_length=100)
    url_imagen = models.CharField('Url imagen', max_length=300)
    fecha_estreno = models.CharField('Url imagen', max_length=15)
    sinopsis = models.CharField('Sinopsis', max_length=500)
