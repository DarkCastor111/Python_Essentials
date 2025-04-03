print('### Función sum')
lista = [1, 2, 3, 4, 5]
print(lista)
# Suma de todos los elementos
resultado = sum(lista)
print(f'Resultado de la suma: {resultado}')
# Con un valor inicial
resultado2 = sum(lista, 20)
print(f'Resultado de la suma con valor inicial: {resultado2}')
print()

print('### Función next')
iterador = iter(lista) # lista se convierte en iterable
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
print(f'Siguiente elemento del iterable: {next(iterador, 40)}')
