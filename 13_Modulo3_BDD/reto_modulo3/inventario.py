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
            except ValueError as e:
                print(f'Opcion inválida')
            except Exception as e:
                print(f'Ocurrió un error : {e}')
    
    def mostrar_menu(self):
        print (f'''Menu:
        1. Listar Productos
        2. Buscar Productos
        3. Añadir Producto
        4. Actualizar Producto
        5. Eliminar Producto
        9. Salir
        ''')
        return int(input('Elije una opción: '))
    
    def ejecutar_opcion(self, opc):
        if opc == 1:
            listado_productos = ProductoDAO.seleccionar_todos()
            print("## Listado de todos los productos")
            for producto in listado_productos:
                print(producto)
        
        elif opc == 2:
            print("## Busqueda de productos por nombre")
            nombre_buscado = input("Introducir el nombre del producto: ")
            productos_encontrados = ProductoDAO.seleccionar_con_nombre(nombre_buscado)
            for producto in productos_encontrados:
                print(producto)

        elif opc == 3:
            print("## Creación nuevo producto")
            nmbr = input('Nombre del nuevo producto: ')
            ctg = input('Categoria del nuevo producto: ')
            prc = input('Precio del nuevo producto: ')
            cdd = input('Cantidad del nuevo producto: ')
            producto_a_crear = Producto(p_nombre=nmbr, p_cantidad=cdd, p_precio=prc, p_categoria=ctg)
            ProductoDAO.crear(producto_a_crear)

        elif opc == 4:
            print("## Actualización producto")
            nmbr = input('Nombre del producto: ')
            productos_encontrados = ProductoDAO.seleccionar_con_nombre(nmbr)
            for producto in productos_encontrados:
                print(producto)

            if len(productos_encontrados) != 1:
                print(f'Error para actualizar el producto {nmbr}')
                return False
           
            prc = input('Nuevo precio del producto: ')
            cdd = input('Nueva cantidad del producto: ')

            producto_a_actualizar = Producto(p_nombre=nmbr, p_cantidad=cdd, p_precio=prc, p_categoria="")
            ProductoDAO.actualizar(producto_a_actualizar)

        elif opc == 5:
            nombre_a_eliminar = input('Nombre completo del producto a eliminar: ')
            ProductoDAO.eliminar_uno(nombre_a_eliminar)


        elif opc == 9:
            print('Regresa Pronto !!')
            return True
        else:
            raise ValueError
        return False

# Principal
if __name__ == '__main__':
    inventario = Inventario()
    inventario.iniciar()