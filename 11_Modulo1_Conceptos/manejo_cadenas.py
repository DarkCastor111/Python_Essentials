# Manejo de cadenas

# Parsing : Dividir una cadena split()
print()
print("### Parsing : Dividir una cadena split()")
cadena = "Hola Mundo"
print(cadena)
palabras = cadena.split()
print(palabras)

palabras2= cadena.split("M")
print(palabras2)

# Buscar y Reemplazar
print()
print("### Buscar y Reemplazar")
abuscar="Mundi"
posicion = cadena.find(abuscar)
print(f"{abuscar} está en la posición: {posicion}")

nueva_cadena = cadena.replace("Mundo", "Amigo")
print(cadena + " => " + nueva_cadena)

# Multiplicación de cadenas
print()
print("### Multiplicación de cadenas")
amultiplicar = "Hola "
resultado = amultiplicar * 5
print(f"Resultado de '{amultiplicar}' * 5 = '{resultado}'")

# Strip : limpiar una cadena
print()
print("### Strip : limpiar una cadena")
alimpiar = "   Hola Mundo.... y    todos.....            "
limpiada = alimpiar.strip()
print(f"Cadena limpiada : '{limpiada}'")
limpiada2 = alimpiar.strip(" .")
print(f"Cadena limpiada2 : '{limpiada2}'")


