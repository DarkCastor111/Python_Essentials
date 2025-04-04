#Crear un archivo
nombre_archivo = "mi_archivo.txt"

# Abrir el archivo en mode escritura ('w')
archivo = open(nombre_archivo, 'w')
archivo.write('Hola como estás\n')
archivo.write('Estoy agregando información al archivo\n')
archivo.close()

# Alternativa utilizando el bloque with
with open(nombre_archivo, 'a') as archivo_with:
    archivo_with.write('Hola de nuevo\n')
    archivo_with.write('Agregando más información al archivo\n')
    # No se necesita close

print(f'Se creó el archivo: {nombre_archivo}')

archivo_nuevo = nombre_archivo

# Modo exclusivo
try:
    with open(archivo_nuevo, 'x') as archivo_with:
        archivo_with.write('Hola de nuevo\n')
        archivo_with.write('Agregando más información al archivo\n')
        print(f'Se creó el archivo: {archivo_nuevo}')
except FileExistsError as e:
    print(f'El archivo {archivo_nuevo} ya existe')
    print(f'Detalle del error: {e}')