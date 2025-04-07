from servicio_snacks import ServicioSnacks
from snack import Snack

class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos_comprados = []

    def iniciar(self):
        salir = False
        print('### Maquina de Snacks ###')
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrió un error : {e}')
    
    def mostrar_menu(self):
        print (f'''Menu:
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar Nuevo Snack
        4. Mostrar Inventario Snacks
        5. Salir
        ''')
        return int(input('Elije una opción: '))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Regresa Pronto !!')
            return True
        else:
            print(f'Opcion inválida: {opcion}')
        return False
    
    def comprar_snack(self):
        id_elejido = int(input(f'Que snack quieres comprar (id)? '))
        snacks = self.servicio_snacks.get_snacks()
        snack_elejido = next((sn for sn in snacks if sn.id_snack == id_elejido), None)
        if snack_elejido:
            self.productos_comprados.append(snack_elejido)
            print(f'Snack encontrado : {snack_elejido}')
        else:
            print(f'Id snack no encontrado: {id_elejido}')

    def mostrar_ticket(self):
        if not self.productos_comprados:
            print('No hay snacks en el ticket')
            return
        total = sum(sn.precio for sn in self.productos_comprados)
        print('### Ticket de venta ###')
        for pr in self.productos_comprados:
            print(f'\t- {pr.nombre} - ${pr.precio:.2f}')
        print(f'\tTotal -> ${total:.2f}')

    def agregar_snack(self):
        nombre = input('Nombre del snack: ')
        precio = float(input('Precio del snack: '))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print('Snack agregado correctamente.')
        

# Principal
if __name__ == '__main__':
    maquina_snack = MaquinaSnacks()
    maquina_snack.iniciar()







