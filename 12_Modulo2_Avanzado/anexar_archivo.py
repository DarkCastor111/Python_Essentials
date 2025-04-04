print('### Anexar información a nuestro archivo')

nombre_archivo = 'mi_archivo.txt'

print()
print('### append')

with open(nombre_archivo, 'a') as archivo_with:
    archivo_with.write('Anexando información 1.... \n')
    archivo_with.write('Anexando información 2.... \n')
    archivo_with.write('Saliendo de anexar \n')

print('Se ha anexado información')