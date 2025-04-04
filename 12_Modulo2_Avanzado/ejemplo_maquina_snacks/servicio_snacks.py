import os.path
from snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'

    def __init__(self):
        self.snacks = []
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo_snacks:
                for linea in archivo_snacks.readlines():
                    (id_sn, nb_sn, pr_sn) = linea.strip().split(',')
                    snack = Snack(nb_sn, float(pr_sn))
                    snacks.append(snack)
        except Exception as e:
            print(f'Error al leer snacks en archivo: {e}')
        return snacks

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('Papas', 2),
            Snack('Refresco', 1.5),
            Snack('Sandwich', 3)
        ]
        self.snacks.extend(snacks_iniciales)
        self.anadir_snacks_archivo(snacks_iniciales)

    def anadir_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo_snacks:
                for snack in snacks:
                    archivo_snacks.write(f'{snack.escribir_snack()}\n')

        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')

    def agregar_snack(self, sn):
        self.snacks.append(sn)
        self.anadir_snacks_archivo([sn])

    def mostrar_snacks(self):
        print('--- Inventario ---')
        for sn in self.snacks:
            print(sn)
    
    def get_snacks(self):
        return self.snacks

