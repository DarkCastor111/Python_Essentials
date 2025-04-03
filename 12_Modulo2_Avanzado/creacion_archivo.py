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


print(f'Se creo el archivo: {nombre_archivo}')