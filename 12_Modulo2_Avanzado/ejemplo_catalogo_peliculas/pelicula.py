class Pelicula:
    contador_id = 0

    def __init__(self, nombre = ''):
        Pelicula.contador_id += 1
        self.id = Pelicula.contador_id
        self.nombre = nombre
    
    def __str__(self):
        return (f'Pelicula: #{self.id} - {self.nombre}')
    
    def escribir_pelicula(self):
        return (f'{self.id},{self.nombre}')