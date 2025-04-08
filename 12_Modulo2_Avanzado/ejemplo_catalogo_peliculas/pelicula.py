class Pelicula:
    contador_id = 0

    def __init__(self, nombre = ''):
        self.nombre = nombre
    
    def __str__(self):
        return (f'Pelicula: {self.nombre}')
    
    def grabar_pelicula(self):
        return (f'{self.nombre}')