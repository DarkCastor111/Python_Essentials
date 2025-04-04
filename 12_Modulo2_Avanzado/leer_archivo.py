print('### Leer archivo con Python')

nombre_archivo = 'mi_archivo.txt'

# Leer el archivo utilisando readlines
print()
print('### readlines')
print('### lista:')
with open(nombre_archivo, 'r') as archivo_with:
    print(archivo_with.readlines())

print()
print('### print el contenido:')
with open(nombre_archivo, 'r') as archivo_with:
    lineas = archivo_with.readlines()
    for linea in lineas:
        print(linea.strip())

# Leer el archivo utilisando read
print()
print('### read')
with open(nombre_archivo, 'r') as archivo_with:
    print(archivo_with.read())