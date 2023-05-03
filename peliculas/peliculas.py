class Peliculas:

    def __init__(self, titulo, titulo_original, url_img, fecha_estreno, sinopsis):
        self.titulo = titulo
        self.titulo_original = titulo_original
        self.url_img = url_img
        self.fecha_estreno = fecha_estreno
        self.sinopsis = sinopsis

    def __str__(self):
        return f"{self.fecha_estreno} - {self.titulo} - {self.sinopsis}"
