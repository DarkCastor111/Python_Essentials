import random
import Comon

Comon.titulo("Bucle while")

a = 0
while a<3:
    print(a, end=' ')
    a += 1
print("\nFuera del while:")
print("a = {}".format(a))


Comon.titulo("Bucle while: break")
a = 5
while a: # True if a <> 0
    print(a, end=' ')
    if a == 2:
        break
    a -= 1
print("\nFuera del while:")
print("a = {}".format(a))

Comon.titulo("Bucle while: continue")
a = 12
while bool(a):
    a -= 1
    if a%2 == 0: # Numero par
        continue
    print (a, end=' ')
print("\nFuera del while:")

Comon.titulo("Bucle while: pass")
a = 6
while a:
    print("    Dentro del while")
    pass
    a -= 1
print("Fuera del while")

Comon.titulo("Bucle while: else")
a = 128
b = a // 2
while b > 1:
    if a % b == 0:
        print("    {} es factor de {}".format(b, a))
        break
    b -= 1
else:
    print("    {} es primo".format(a))
print("Fuera del while")

Comon.titulo("Bucle for")
print("\nFor: Lista de String")
for s in ["Me", "gusta", "Python!"]:
    print(s, end=' ')
print("\nFin del for")

print("\nFor: Lista de Numeros")
a = 0
for x in [0, 1, 2, 3, 4]:
    a += x
print("Fin del for")
print("a = {}".format(a))

print("\nFor: Un String")
for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(c, end='|')
print("\nFin del for")

print()

Comon.titulo("Diccionario")
dict_keys = ['nombre', 'apellidos', 'edad']
dict_values = ['Guido', 'van Rossum', '60']
dict1 = dict(zip(dict_keys, dict_values)) # Creamos el diccionario
for k in dict1:
    info = '{}: {}'.format(k, dict1[k]) # Texto formateado con claves y valores
    print(info)
print()
for k, v in dict1.items(): # d.items devuelve tupla con clave, valor
    print('{}: {}'.format(k, v))
print()
for k in dict1.keys():
    print(k, end = ' ')
print()
for v in dict1.values():
    print(v, end = ' ')
print()

print("Keys : ", type(dict1.keys()), " : ", dict1.keys())
print("Values : ", type(dict1.values()), " : ", dict1.values())
print("Items : ", type(dict1.items()), " : ", dict1.items())

# Acceder a una vista de diccionario
print("Secundo elemento de las llaves :", list (dict1.keys())[1])

Comon.titulo("Tuplas")
t = [(1, 2), (3, 4), (5, 6)]
for x, y in t:
    print ("x + y = ", x + y)
print()
list_a = [10, 20, 30, 40]
list_b = [5, 25, 50, 10]
for a, b in zip(list_a, list_b):
    m = max(a, b) # max(a, b) devuelve el máximo entre a y b
    print("maximo entre {} y {} = ".format(a, b), m)

Comon.titulo("Range")
print("range(5) : ", end = '')
for n in range(5):
    print(n, end = ", ")
print()
print("range(-5, 5) : ", end = '')
for n in range(-5, 5):
    print(n, end = ", ")
print()
print("range(-5, 5, 2) : ", end = '')
for n in range(-5, 5, 2): # Elementos -5 a 5 en saltos de 2
    print(n, end = ", ")
print()

Comon.titulo("Ejemplos Pythónicos")



letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
vocales = "AEIOU"

random.shuffle(letras)

print("letras (list) : ", letras)
print("letras (string) : ", ''.join(letras))

trozo1 = letras[:8]
trozo2 = letras[8:16]
trozo3 = letras[16:]

# Versión no Pythónica
print("Recorrer varias listas simultáneamente: Versión no Pythónica:")
for i in range(len(trozo1)):
    print(trozo1[i] + trozo2[i] + trozo3[i], sep='', end = ' ')
print()
# Versión Pythónica
print("Recorrer varias listas simultáneamente: Versión Pythónica:")
for a, b, c in zip(trozo1, trozo2, trozo3):
    print(a + b + c, end =' ')
print()
# Versión no Pythónica
print("Búsquedas de indices: Versión no Pythónica:")
for i in range(len(letras)):
    if letras[i] in vocales:
        print("{} en la posición {}".format(letras[i], i))
# Versión no Pythónica
print("Búsquedas de indices: Versión Pythónica:")
for i, letra in enumerate(letras):
    if letra in vocales:
        print("{} en la posición {}".format(letra, i))

Comon.titulo("enumerate")
abcde = sorted(letras)[:5]
print("enumerate(letras) = ", list(enumerate(letras)))
print("enumerate(abcde) = ", list(enumerate(abcde)))
print("enumerate(abcde, 10) = ", list(enumerate(abcde, 10))) #Empezando en 10

Comon.titulo("Iteradores")

for num in [1, 2, 3, 4, 5, 6]:
    print(num ** 2, end= ' ')
print()
for num in [12, 38, 99, 1]:
    print(num / 2, end= ' ')
print()
for letra in 'Python':
    print(letra.upper(), end=' ')
print()
print()

zen = '''\
Bello es mejor que feo.
Explícito es mejor que implícito.
Simple es mejor que complejo.
Complejo es mejor que complicado.
'''

f = open('short.zen.txt', 'w')
f.writelines(zen) # Escribe el fichero
f.close() # Cierra el fichero

f = open('short.zen.txt', 'r')
print("f.readline() : ", f.readline())
print("f.readline() : ", f.readline())
print("f.__next__() : ", f.__next__())
print("next(f) : ", next(f)) # Equivalente a f.__next__()
f.close()

f = open('short.zen.txt', 'r')
for linea in f:
    print(linea.upper(), end='')
print()
lista = [1, 2, 3]
lista_iter = lista.__iter__() # o iter(lista)
print("lista : ",lista)
print("lista_iter : ", lista_iter)
print("lista_iter.__next__() : ", lista_iter.__next__())
print("next(lista_iter) : ", next(lista_iter))
