from cliente_dao import ClienteDAO
from cliente import Cliente

class ZonaFit:
    def iniciar(self):
        salir = False
        print('### Gestión de Zona Fit ###')
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrió un error : {e}')
    
    def mostrar_menu(self):
        print (f'''Menu:
        1. Listar Clientes
        2. Añadir un Cliente
        3. Actualizar un Cliente
        4. Eliminar un Cliente
        9. Salir
        ''')
        return int(input('Elije una opción: '))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            listado_clientes = ClienteDAO.seleccionar_todos()
            for cli in listado_clientes:
                print(cli)

        elif opcion == 2:
            print('## Añadir un cliente ##')
            nom = input('Nombre del nuevo cliente: ')
            apel = input('Apellido del nuevo cliente: ')
            mem = input('Membresía del nuevo cliente: ')
            nuevo_cliente = Cliente(p_nombre=nom, p_apellido=apel, p_membresia=mem)
            ClienteDAO.crear(nuevo_cliente)

        elif opcion == 3:
            print('## Modificar un cliente ##')
            id = input('id del cliente a actualizar: ')
            cliente_a_actualizar = ClienteDAO.seleccionar_uno_con_id(id)

            nom = input('Nombre del cliente a actualizar (return si no cambia): ')
            if nom != "":
                cliente_a_actualizar.nombre = nom
            apel = input('Apellido del cliente a actualizar (return si no cambia): ')
            if apel != "":
                cliente_a_actualizar.apellido = apel
            mem = input('Membresía del cliente a actualizar (return si no cambia): ')
            if mem != "":
                cliente_a_actualizar.membresia = mem

            ClienteDAO.actualizar(cliente_a_actualizar)
            
        elif opcion == 4:
            print('## Eliminar un cliente ##')
            id = input('id del cliente a eliminar: ')
            cliente_a_eliminar = Cliente(p_id=id)
            ClienteDAO.eliminar_uno(cliente_a_eliminar)

        elif opcion == 9:
            print('Regresa Pronto !!')
            return True
        else:
            print(f'Opcion inválida: {opcion}')
        return False


# Principal
if __name__ == '__main__':
    catalogo_peli = ZonaFit()
    catalogo_peli.iniciar()







