import pandas
from peliculas import *

def cargar_archivo(path):
    data = pandas.read_csv(path)

    return data


def llenar_diccionario(data):
    dictionary = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
        10: [],
        11: [],
        12: [],
    }

    data_len = len(data)
    for x in range(data_len):
        titulo = data["titulo"][x]
        titulo_original = data["titulo_original"][x]
        url_img = data["url_imagen"][x]
        fecha_estreno = data["fecha_estreno"][x].strip()
        sinopsis = data["sinopsis"][x]

        nueva_pelicula = Peliculas(titulo, titulo_original, url_img, fecha_estreno, sinopsis)
        mes = int(nueva_pelicula.fecha_estreno[6])
        dictionary[mes].append(nueva_pelicula)

    return dictionary

def mostrar_diccionario(diccionario):
    mes = int(input("Introduce el mes de la película: "))
    if len(diccionario[mes]) > 0:
        print(f"Mes: {mes}")
        for y in range(len(diccionario[mes])):
            if diccionario[mes][y] != None:
                print(diccionario[mes][y])
    else:
        print("No hay películas registradas en ese mes")

if __name__ == '__main__':
    data = cargar_archivo("estrenos.csv")
    diccionario = llenar_diccionario(data)
    mostrar_diccionario(diccionario)




