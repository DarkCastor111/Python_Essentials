import os, os.path
from pelicula import Pelicula

class ServicioCatalogo:
    NOMBRE_ARCHIVO = './12_Modulo2_Avanzado/ejemplo_catalogo_peliculas/peliculas.txt'

    def __init__(self):
        self.peliculas = []
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.leer_peliculas()
            print(f'## Inicializacion : archivo encontrado => {self.peliculas}')
        else:
            self.inicializar()
            print('## Inicializacion : archivo NO encontrado')

    def inicializar(self):
        pelis_init = [
            Pelicula('James Bond'),
            Pelicula('Star Wars'),
            Pelicula('Shrek'),
        ]
        for pel in pelis_init:
            self.peliculas.append(pel)
            self.grabar_pelicula(pel)

    def leer_peliculas(self):
        try:
            with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo_peliculas:
                for linea_peli in archivo_peliculas.readlines():
                    (id_peli, nb_peli) = linea_peli.strip().split(',')
                    self.peliculas.append(Pelicula(nb_peli))
        except Exception as e:
            print(f'Error al leer el archivo {self.NOMBRE_ARCHIVO} : {e}')


    def mostrar_peliculas(self):
        for peli in self.peliculas:
            print(peli)

    def grabar_pelicula(self, peli):
        try:
            self.peliculas.append(peli)
            with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo_peliculas:
                archivo_peliculas.write(f'{peli.escribir_pelicula()}\n')
        except Exception as e:
            print(f'Error al guardar la peli {peli.escribir_pelicula()} en archivo: {e}')

    def eliminar_catalogo(self):
        os.remove(self.NOMBRE_ARCHIVO)


