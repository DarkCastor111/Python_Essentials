
capitulo = 0

def titulo(_tit):
    global capitulo
    capitulo += 1
    print()
    print("#####################################")
    print("##", capitulo, "##  " + _tit)
    print("#####################################")


"""
Definición
""" 
titulo("Definición")

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.

def en_pantalla(frase1, frase2):
    print("frase1, frase2=", frase1, frase2) # "return" no es obligatorio
    print("frase1 + frase2=",frase1 + frase2)

x = suma(2, 3) # Llamada a la función. Hay que pasarle dos parámetros.
print(x) # Resultado: 5 (no inscrito)

"""
    Poliformismo
"""
titulo("Poliformismo")
en_pantalla(3, 4)
en_pantalla(2.7, 4.0)
en_pantalla("También es posible", "agregar textos")
#en_pantalla('El resultado es :', suma(2, 3)) # Error porque no se puede concatenar int con str

"""
    Funciones anidadas
"""
titulo("Funciones anidadas")
def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) 
    f2(b) # Llamamos a f2 desde f1

f1('Python') # Llamamos a f1

"""
    Recursividad
"""
titulo("Recursividad")
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1

print ("factorial(5)=", factorial(5))

"""
    Devolviendo múltiples valores simultáneamente
"""
titulo("Devolviendo múltiples valores simultáneamente")

def maxmin(lista):
    return max(lista), min(lista) # Devuelve una tupla de 2 elementos

liste = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(liste) # Desempaqueta la tupla en 2 variables
print(minimo, maximo, sep= ' - ')

"""
    Experimenta
    Realiza una función que realice la descomposición en
    factores de un número. Deberá devolver una lista con
    los factores de dicho número. Recordad que la
    descomposición en factores de un número consiste
    en hallar el conjunto de números primos cuya
    multiplicación dé dicho número como resultado.
"""
"""
    Ámbito de una variable
"""
titulo("Ámbito de una variable")
a = 'Python' #Scope global (al módulo)
print('Valor fuera:', a)

def funcion_local():
    a=33
    print('Valor dentro:', a) #Scope local a la función

funcion_local()
print('Valor fuera:', a)

"""
    La regla LEGB
"""
titulo("La regla LEGB")
G = 'G: Esta variable es de ámbito Global'
def f1():
    E='E: Esta variable es local a f1. Enclosing a f2 y f3'
    def f2():
        L = 'L: Esta variable es local a f2'
        E = 'E: valor local a f2'
        G = 'G: valor local a f2'
        print(L, E, G, sep = '\n')
    def f3():
        print(E, G, sep = '\n')
    f2()
    f3()
f1()

"""
    Argumentos de las funciones
"""
titulo("Argumentos de las funciones")

def minimo(_list):
    _list[0] += 1000 # Modificamos la lista en el interior
    return min(_list)

list_ArgFunc = [1, 2, 3]
print(list_ArgFunc)
print(minimo(list_ArgFunc)) # Modifica la lista aquí
print(list_ArgFunc)

"""
    Formas de paso de argumentos: posición.
"""
titulo("Formas de paso de argumentos: posición.")

def f1(a, b, c):
    print("f1(1, 2, 3) => ",a, b, c)

f1(1, 2, 3)

"""
    Formas de paso de argumentos: palabras clave.
"""
titulo("Formas de paso de argumentos: palabras clave.")

def f2(a, b, c):
    print("f2(c=12, a=10, b=100) => ", a, b, c)

f2(c=12, a=10, b=100)

"""
    Formas de paso de argumentos: valores por defecto.
"""
titulo("Formas de paso de argumentos: valores por defecto.")

def f3(a, b=10, c=30):
    print("f3(a, b=10, c=30) => ", a, b, c)

f3(1)
f3(1, 12)
f3(1, 12, 19)

"""
    Formas de paso de argumentos: colecciones.
"""
titulo("Formas de paso de argumentos: colecciones.")

def f4(*args): # Acepta número arbitrario de argumentos
    print(args)

f4() # Si no hay argumentos, args es una tupla vacía
f4(1)
f4(1, 2)
f4(1, 2, 3, 4, 5, 6)
f4(1, 2, [3, 4, 5])

"""
    Formas de paso de argumentos: diccionario.
"""
titulo("Formas de paso de argumentos: diccionario.")

def f5(**Kargs): # Acepta número de argumentos por nombre
    print(Kargs)

f5() # Si no hay argumentos, Kargs es un diccionario vacío
f5(a=1)
f5(a=1, b=2)
f5(a=1, c=3, b=2)

"""
    Formas de paso de argumentos: Desempaquetando.
"""
titulo("Formas de paso de argumentos: Desempaquetando.")

def f6(a, b, c, d):
    print(a, b, c, d)

argumentos1 = {'b':20, 'a':1, 'c':300, 'd':4000}
f6(**argumentos1) # Desempaquetando diccionario argumentos con **

argumentos2 = {'b':200, 'c':300, 'd':400}
f6(10, **argumentos2) # Podemos combinar argumentos posicionales con dict

"""
    Formas de paso de argumentos: keyword-only.
"""
titulo("Formas de paso de argumentos: keyword-only.")

def f7(a, *, b, c): # Define 'b' y 'c' como keyword-only con el *
    print(a, b, c)

f7(1, b=10, c=100)
#f7(1, 10, 100) # Error al no pasar argumentos Keyword-only

"""
    Formas de paso de argumentos: opcionales.
"""
titulo("Formas de paso de argumentos: opcionales.")

def f8(a, *b, c): # Hay que pasar 'c' por clave obligatoriamente
    print(a, b, c)

f8(1, c=2)
f8(1, 2, c=3)
f8(1, 2, 3, 4, 5, c=10)

"""
    Experimenta
    Crea una función log que acepte cualquier número de
    argumentos y los imprima por pantalla en una misma
    línea. La línea debe empezar con el prefijo "LOG: ".
    
    Modifica la función log para que usuario pueda
    especificar cualquier prefijo que desee.
    
    Modifica la función log para que el prefijo tenga el
    valor por defecto "LOG: ".
    
    Modifica la función log para que el usuario pueda
    establecer tanto prefijo como separador entre
    argumentos. Ambos deben pasarse sólo por los
    nombres (no por posición) "sep" y "prefix". No hace
    falta que estos tengan valor por defecto.
    
    Modfica la función log para que ahora "sep" y "prefix"
    tengan un valor por defecto.
    
    Modifica la función log para que acepte el siguiente
    diccionario. Recuerda que hay que pasarlo
    desempaquetándolo con la sintaxis de doble
    asterisco (**).
"""
"""
    Formas de paso de argumentos: experimenta.
"""
titulo("Formas de paso de argumentos: experimenta.")

def f_log(*args, pref="LOG:", sep):
    print(pref, end=" ")
    print(args, sep=sep)

f_log( 1, 2, 4, 5, 8, 10, pref="INFO:", sep="|")
f_log([1, 2], "toto", "tata", 3, 4, sep=",")


