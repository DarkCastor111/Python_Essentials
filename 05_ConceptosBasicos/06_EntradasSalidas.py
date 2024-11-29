"""
# Entrada input del usuario
nombre = input('Introduce tu nombre: ') #Considerado como un string => int(), float(), ...
# Salida
print("Hola, " + nombre)
print(type(nombre))

# Entrada por parte del usuario como número entero
num = input('Introduce un número: ')
add = int(num)+1
# Salida
print(add)

# Pedir varios valores de una sola vez
a, b, c = map(int, input("Introduzca los números: ").split())
print("Los números son: ", end = " ")
print("a = ", a)
print("b = ", b)
print("c = ", c)

# Entrada de datos en listas, conjuntos, tuplas
# 1. Elementos de List/Set uno por uno
l1 = list()
s1 = set()
# tamano_lista = int(input("Introduzca el tamaño de la lista: "))
# tamano_set = int(input("Introduzca el tamaño del Set: "))
print("Introduzca los elementos de la lista: ")
for i in range(0, 1):
    l1.append(int(input()))
print("Introduzca los elementos del set: ")
for i in range(0, 5):
    s1.add(int(input()))
print(l1)
print(s1)

# métodos map() for list() / set()
l2 = list(map(int, input("Introduzca los elementos de la lista:").split()))
s2 = set(map(int, input("Introduzca los elementos del Set: ").split()))
print(l2)
print(s2)


# Entrada de datos en una tupla
# => Hay que convertirla en list
t3 = (2, 3, 4, 5, 6)
print("Tupla inicial", t3)

l3 = list(t3)
l3.append(int(input("Introduzca el nuevo elemento: ")))
t3 = tuple(l3)
print("Tupla final")
print(t3)
"""

# Salida de datos en Python

# Demostración de la función print()
print("GFG")
# Demostración de la función print() con espacios
print('G', 'F', 'G')

print("GFG", end = "@")
print('G', 'F', 'G', sep = "#")

# Salida de datos con formato

# Salida con f
name = "Antonio"
print(f'hola {name}!. Qué tal?')

# Salida con format
a = 20
b = 10
# Suma
sum = a+b
# Resta
sub = a-b
# Salida
print('El valor de a es {} y b es {}'.format(a,b))
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a, value_b=b, sub_value=sub))

# Uso del operador %
num = int(input("Introduzca un número: "))
add = num+5
# Salida
print("La suma es %f" %add)
