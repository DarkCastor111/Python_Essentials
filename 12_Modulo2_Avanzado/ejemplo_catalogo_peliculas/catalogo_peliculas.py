from servicio_catalogo import ServicioCatalogo
from pelicula import Pelicula

class CatalogoPeliculas:
    def __init__(self):
        self.servicio_catalogo = ServicioCatalogo()

    def iniciar(self):
        salir = False
        print('### Catalogo de peliculas ###')
        self.servicio_catalogo.mostrar_peliculas()
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
            self.servicio_catalogo.mostrar_peliculas()
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







