from servicio_catalogo import ServicioCatalogo
from pelicula import Pelicula

class CatalogoPeliculas:
    def __init__(self):
        self.servicio_catalogo = ServicioCatalogo()

    def iniciar(self):
        salir = False
        print('### Catalogo de peliculas ###')
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrió un error : {e}')
    
    def mostrar_menu(self):
        print (f'''Menu:
        1. Agregar Película
        2. Listar Películas
        3. Eliminar Catalogo
        4. Salir
        ''')
        return int(input('Elije una opción: '))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            nombre = input('Nombre de la pelicula: ')
            nueva_pelicula = Pelicula(nombre)
            self.servicio_catalogo.grabar_pelicula(nueva_pelicula)
            print('Pelicula agregada correctamente.')
        elif opcion == 2:
            pelis_catalogo = self.servicio_catalogo.leer_peliculas()
            numero = 0
            for peli in pelis_catalogo:
                numero += 1
                print(f'#{numero:02} {peli}')
        elif opcion == 3:
            self.servicio_catalogo.eliminar_catalogo()
            print('Catalogo eliminado correctamente.')
        elif opcion == 4:
            print('Regresa Pronto !!')
            return True
        else:
            print(f'Opcion inválida: {opcion}')
        return False


# Principal
if __name__ == '__main__':
    catalogo_peli = CatalogoPeliculas()
    catalogo_peli.iniciar()







