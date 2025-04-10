import os, os.path
from contacto import Contacto

class GestionContactos:

    NOMBRE_ARCHIVO = "contactos.txt"

    def __init__(self):
        self.contactos = []
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.contactos = self.leer_contactos()
        else:
            print(f'WARNING: Fichero {self.NOMBRE_ARCHIVO} no encontrado')

    def leer_contactos(self):
        contactos_leidos=[]
        try:
            with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo_contactos:
                for linea in archivo_contactos.readlines():
                    (cto_nmb, cto_tlf, cto_correo ) = linea.strip().split(',')
                    contacto = Contacto(cto_nmb, cto_tlf, cto_correo)
                    contactos_leidos.append(contacto)
        except Exception as e:
            print(f'ERROR: al leer el archivo {self.NOMBRE_ARCHIVO}: {e}')
        return contactos_leidos

    def guardar_contacto(self, contacto_a_guardar):
        # Control: contacto ya existente (correo electronico) ?
        for c in self.contactos:
            if contacto_a_guardar.correo == c.correo :
                print(f'ERROR: El contacto {c.nombre} ya existe con el correo {contacto_a_guardar.correo}')
                return
        try:
            self.contactos.append(contacto_a_guardar)
            with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo_contactos:
                archivo_contactos.write(contacto_a_guardar.to_string_archivo())
            print(f'INFO: {contacto_a_guardar} => guardado')
        except Exception as e:
            print(f'ERROR: escribiendo en el archivo {self.NOMBRE_ARCHIVO}: {e}')

    def eliminar_contacto(self, correo_contacto_a_eliminar):
        contactos_iniciales = self.contactos.copy()
        self.contactos = []
        os.remove(self.NOMBRE_ARCHIVO)
        encontrado = False
        for c in contactos_iniciales:
            if c.correo == correo_contacto_a_eliminar:
                # Eliminación dentro de la lista de contactos
                encontrado = True
                print(f'INFO: {c} => eliminado')
            else:
                self.guardar_contacto(c)
        
        if not encontrado:
            print(f'WARNING: {correo_contacto_a_eliminar} no encontrado')

    def mostrar_contactos(self):
        if self.contactos == []:
            print('WARNING: No hay contactos')
            return
        else:
            for c in self.contactos:
                print(c)

    def buscar_contacto(self, nombre_contacto_a_buscar):
        encontrado = False
        for c in self.contactos:
            if nombre_contacto_a_buscar.upper() in c.nombre.upper() :
                print(f'INFO: {c} => encontrado')
                encontrado = True
        if not encontrado:
            print(f'WARNING: Contacto "{nombre_contacto_a_buscar}" no encontrado')

    def anadir_contacto(self, nombre_contacto, telefono_contacto, correo_contacto):
        try:
            contacto = Contacto(nombre_contacto, telefono_contacto, correo_contacto)
            self.guardar_contacto(contacto)
        except ValueError as e:
            print(f'ERROR: {e}')
            return

    
"""    
print()
print('Inicializacion:')
gestionContactos = GestionContactos()

print()
print('Creando contactos:')
gestionContactos.anadir_contacto('Toto4', '555421236', 'toto4@tata.com')
gestionContactos.anadir_contacto('Toto5', '555421236', 'toto5@tata.com')
gestionContactos.anadir_contacto('Toto6', '555123', 'toto6@tata.com')

print()
gestionContactos.mostrar_contactos()

print()
print('Eliminando contacto:')
gestionContactos.eliminar_contacto('toto5@tata.com')


print()
gestionContactos.mostrar_contactos()

print()
gestionContactos.buscar_contacto('tota4')
"""
        