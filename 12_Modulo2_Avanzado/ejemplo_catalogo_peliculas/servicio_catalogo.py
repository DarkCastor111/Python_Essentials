import os, os.path
from pelicula import Pelicula

class ServicioCatalogo:
    NOMBRE_ARCHIVO = './12_Modulo2_Avanzado/ejemplo_catalogo_peliculas/peliculas.txt'

    def __init__(self):
        pass

    def leer_peliculas(self):
        peliculas = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo_peliculas:
                for linea_peli in archivo_peliculas.readlines():
                    nb_peli = linea_peli.strip()
                    peliculas.append(Pelicula(nb_peli))
        except Exception as e:
            print(f'Error al leer el archivo {self.NOMBRE_ARCHIVO} : {e}')
        return peliculas

    def grabar_pelicula(self, peli):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo_peliculas:
                archivo_peliculas.write(f'{peli.grabar_pelicula()}\n')
        except Exception as e:
            print(f'Error al guardar la peli {peli.grabar_pelicula()} en archivo: {e}')

    def eliminar_catalogo(self):
        os.remove(self.NOMBRE_ARCHIVO)


