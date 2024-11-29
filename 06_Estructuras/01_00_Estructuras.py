import Comon

Comon.titulo("Listas.")

def hola():
    print("Hola Mundo")

miLista1=["Angel", 43, 667767250, hola]
miLista2 = [22, True, "una lista", [1, 2]]
miLista3 = list('Python')
miLista4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("miLista1 =", miLista1)
print("miLista2 =", miLista2)
print("type(miLista1) = ", type(miLista1))

print("miLista3 =", miLista3)

print("miLista3[0] =", miLista3[0])

print("miLista2[3][1] =", miLista2[3][1])

print("miLista2[:] =", miLista2[:])
print("miLista2[0:2] =", miLista2[0:2])
print("miLista4[0:8:3] =", miLista4[0:8:3])

print("miLista2[-2:] =", miLista2[-2:])

print("// Operadores")

print("miLista3 == miLista2 ?", miLista3 == miLista2)
print("22 in miLista2 ? ", 22 in miLista2)
print("2 in miLista2 ?", 2 in miLista2)
print("[1, 2] in miLista2 ?", [1, 2] in miLista2)

print("miLista3 * 2 =", miLista3 * 2)

Comon.titulo("Tuplas.")

miTupla1 = ("Angel", 43, 667767250, hola)
miTupla2 = ("Plátano",) # Un elemento unico
miNoTupla3 = (44)
miTupla4 = tuple(("apple", "banana", "cherry"))


print("miTupla1 =", miTupla1)
print("miTupla4 =", miTupla4)
print("miTupla1[1] =", miTupla1[1])
print("miTupla1[-2:] =", miTupla1[-2:])
print("miTupla1[1:3] =", miTupla1[1:3])

print("// Cambiar valores de una tupla => list")

miListaTupla = list(miTupla1)
miListaTupla.append("kiwi")
print("miListaTupla =", miListaTupla)
miTupla1 = tuple(miListaTupla)
print("miTupla1 =", miTupla1)

print("// Recorrer una tupla => for")
for x in miTupla1:
    print(x, end = "|")
print()

print()
print("'kiwi' in miTupla1 ?", 'kiwi' in miTupla1)
print("len(miTupla1) = ", len(miTupla1))
print("miTupla1.count('kiwi') = ", miTupla1.count('kiwi'))
print("miTupla1 + miTupla2 = ", miTupla1 + miTupla2)

print()
print("miTupla2 =", miTupla2)
print("type(miTupla2) =", type(miTupla2))
print("miNoTupla3 =", miNoTupla3)
print("type(miNoTupla3) =", type(miNoTupla3))

Comon.titulo("Diccionarios.")

dicc1 = {
    "Nombre":"Santiago",
    "Apellido":"Hernandez",
    "Pais":"España",
    "Ciudad":"Madrid"
}

# Otra forma de definir diccionarios con la funcion dict()
dicc2 = dict(
    Nombre="François",
    Apellido="Dumont",
    Pais="France",
    Ciudad="Paris"
)

print("dicc1 = ", dicc1)
print("dicc2 = ", dicc2)