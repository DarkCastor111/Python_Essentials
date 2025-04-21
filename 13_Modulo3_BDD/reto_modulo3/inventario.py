from producto import Producto
from producto_dao import ProductoDAO

class Inventario:
    def iniciar(self):
        salir = False
        print('### Gestión de Inventario ###')
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrió un error : {e}')
    
    def mostrar_menu(self):
        print (f'''Menu:
        1. Listar Productos
        9. Salir
        ''')
        return int(input('Elije una opción: '))
    
    def ejecutar_opcion(self, opc):
        if opc == 1:
            listado_productos = ProductoDAO.seleccionar_todos()
            for cli in listado_productos:
                print(cli)

        elif opc == 9:
            print('Regresa Pronto !!')
            return True
        else:
            print(f'Opcion inválida: {opc}')
        return False

# Principal
if __name__ == '__main__':
    inventario = Inventario()
    inventario.iniciar()