import Comon


Comon.titulo("Diccionarios")

miDiccionario = {
    "brand": "Ford",
    "model": "Mustang",
    "year": [1964, 1965, 1966, 1969]
}

miDiccionario2 = dict(brand = "Renault", model="R12", year="1973")


print("miDiccionario : ", miDiccionario)
print("miDiccionario2 : ", miDiccionario2)
print("miDiccionario.keys() : ", miDiccionario.keys())
print("miDiccionario.values() : ", miDiccionario.values())
print("len(miDiccionario : ", len(miDiccionario))
print("miDiccionario['brand'] : ", miDiccionario["brand"])

# Añadir elementos
miDiccionario["color"] = "red"
print("miDiccionario : ", miDiccionario)
print()
# Eliminar elementos
print("miDiccionario.pop('brand') : ", miDiccionario.pop('brand'), "=> miDiccionario : ", miDiccionario)

print("miDiccionario.popitem() : ", miDiccionario.popitem(), " => miDiccionario : ", miDiccionario)

del miDiccionario["model"]
print("del miDiccionario['model'] => miDiccionario : ", miDiccionario)
miDiccionario.clear()
print("miDiccionario.clear() => miDiccionario : ", miDiccionario)

print()


lista_claves=["nombre", "edad"]
lista_valores=["Angel", 49]
miDicc2 = dict(zip(lista_claves, lista_valores))
print("miDicc2 : ", miDicc2)

miList2 = list(zip(lista_claves, lista_valores))
print("miList2 : ", miList2)

print("'nombre' in miDicc2 ? ", 'nombre' in miDicc2)

i=0
for x in miDicc2:
    i+=1
    print("miDicc2 key-{} : ".format(i), x)
    print("miDicc2 value-{} : ".format(i), miDicc2[x])
print()

i=0
for x in miDicc2.values():
    i+=1
    print("miDicc2 value-{} : ".format(i), x)
print()

i=0
for x, y in miDicc2.items():
    i+=1
    print("miDicc2 items-{} : ".format(i), x, y)

# Copiar un diccionario
miNewDicc = miDicc2.copy()
miNewDicc2 = dict(miDicc2)

print ("miNewDicc : ", miNewDicc)
print ("miNewDicc2 : ", miNewDicc2)

