import Comon
# VARIABLES
# Lo ideal es declarar e inicializar siempre las variables.
# -----------------------------------------------------------
# En Python podemos asignar una variable a otra variable diferente.


Comon.titulo("Declaración e Inicialización")
var = "Hola mundo"
var2 = var
print("var= ", var)
print("var2= ", var2)
# La variable var y var2 apuntan a la misma cadena de texto Hola mundo
# Los nombres de las variables en Python pueden tener cualquier longitud y
# pueden consistir en letras mayúsculas y minúsculas (A-Z, a-z), dígitos (0-9) y
# el carácter de subrayado (_). Cualquier otro carácter dará error:
#var& = "Hola mundo"
var_ = "Hola mundo"

# Aunque el nombre de una variable puede contener dígitos, el primer carácter de
# un nombre de variable no puede ser un dígito.
#2var = "Hola mundo"
var7 = "Hola mundo"

# El nombre de las variables en Python es sensible a mayúsculas y minúsculas
Var3 = "Hola mundo"
#print(var3) # Error, no se encuentra var3
print("Var3= ", Var3)

# Declaración de variable numérica entera:
n_edad = 47
print("variable numérica entera:: n_edad = ", n_edad)

# Declaración de variable numérica de coma flotante:
n_numero = -23.5245
print("variable numérica de coma flotante:: n_numero = ", n_numero)

# Declaración de variable de tipo string:
s_nombre = 'Manolo es "amigo" mío'
print("variable de tipo string:: s_nombre = ", s_nombre)

# Declaración de variable de tipo string en varias líneas:
s_textoLargo = """Esto es un mensaje
...con tres saltos
...de linea"""
print("variable de tipo string en varias líneas:: s_textoLargo = ", s_textoLargo)

# Sobreescribimos el valor de la variable n_edad y ahora la ponemos como string:
n_edad = "47"
print("n_edad en string:: n_edad = ", n_edad)

# Declaración de constante:
NUMEROPI = 3.14159
print("constante:: NUMEROPI = ", NUMEROPI)

Comon.titulo("Declaración de un boolean")
# Declaración de un boolean
es_True = True
es_False = False
print("Boolean:: es_True es_False = ", es_True, es_False)

# True = 1 y False = 0
print("Boolean:: True == 1 ?", True == 1)
print("Boolean:: False == 0 ?", False == 0)
print("Boolean:: True + 2 = ", True + 2)
# Cuando se valida una condición , Python devuelve True o False:
print("Boolean:: 10 > 9 ?", 10 > 9)
print("Boolean:: 10 == 9 ?", 10 == 9)
print("Boolean:: 10 < 9 ?", 10 < 9)

# Declaración múltiple
Comon.titulo("Declaración múltiple")
# En una sola instrucción, estamos declarando tres variables: a, b, c, y asignándoles un valor concreto a cada una.
a, b, c = 'string', 15, True
print("Declaración múltiple:: a, b, c =", a, b, c)
# Sería como poner:
a = 'string'
b = 15
c = True
print("Declaración individual:: a, b, c =", a, b, c)

# Para verificar el tipo de cualquier objeto en Python, usamos la función type() :
Comon.titulo("Verificar el tipo")
print("type(n_edad) = ", type(n_edad))
print("type(n_numero) = ", type(n_numero))
print("type(s_nombre) = ", type(s_nombre))
print("type(NUMEROPI) = ", type(NUMEROPI))
print("type(es_True) = ", type(es_True))
print("type(es_False) = ", type(es_False))

# Forzado de tipo, CASTING:
Comon.titulo("Casting")

# Forzado de tipo Enteros:
x = int(1) # x Valdrá 1
y = int(2.8) # y Valdrá 2
z = int("3") # z Valdrá 3
print("Casting:: x, y, z =", type(x), x, type(y), y, type(z), z)

# Forzado de tipo Float:
x = float(1) # x Valdrá 1.0
y = float(2.8) # y Valdrá 2.8
z = float("3") # z Valdrá 3.0
w = float("4.2") # w Valdrá 4.2
print("Casting:: x, y, z, w =", type(x), x, type(y), y, type(z), z, type(w), w)

# Forzado de tipo string:
x = str("s1") # x Valdrá 's1'
y = str(2) # y Valdrá '2'
z = str(3.0) # z Valdrá '3.0'
print("Casting:: x, y, z =", type(x), x, type(y), y, type(z), z)

# CASTING. Reconversión de tipos:
# Casting de int a float:
n_numero = 13
print("Casting:: n_numero : ", type(n_numero), n_numero)
n_numero_2 = float(n_numero)
print("Casting:: n_numero_2 = float(n_numero) : ", type(n_numero_2), n_numero_2)

# Casting de float a int:
n_numero_3 = 24.876
print("Casting:: n_numero_3 : ", type(n_numero_3), n_numero_3)
n_numero_4 = int(n_numero_3)
print("Casting:: n_numero_4 = int(n_numero_3) : ", type(n_numero_4), n_numero_4)

# Casting de string a int
s_texto = "13"
print("Casting:: s_texto : ", type(s_texto), s_texto)
n_numero_5 = int(s_texto)
print("Casting:: n_numero_5 = int(s_texto) : ", type(n_numero_5), n_numero_5)

# Casting de int a string
n_numero_6 = 27
print("Casting:: n_numero_6 : ", type(n_numero_6), n_numero_6)
s_texto_2 = str(n_numero_6)
print("Casting:: s_texto_2 = str(n_numero_6) : ", type(s_texto_2), s_texto_2)


# COMENTARIOS
Comon.titulo("Comentarios")
# Los comentarios son anotaciones que pondremos en nuestro código que el programa no va a tener en cuenta.
# Existen dos tipos de comentarios:

# Esto es un comentario de una línea

"""Esto es un comentario
que me va a ocupar
varias líneas"""


# TRABAJAR CON STRINGS
Comon.titulo("String")
"""Los strings son secuencias de caracteres de texto.
Todos los objetos en Python se engloban en dos categorías: mutables o inmutables.
Los tipos básicos mutables son las listas, los diccionarios y los sets.
Los tipos básicos inmutables son los números, los strings y las tuplas.
Los objetos mutables pueden ser cambiados en el mismo objeto, mientras que los inmutables no.
"""
# Para concatenar textos se hace con “+” o simplemente con una coma.
# Si ponemos coma nos pone entre los textos un espacio, con + no lo hace.
print("String:: Esta frase" , "termina aquí.")
print("String:: Esta frase" + "termina aquí.")
# Contatenación y multiplicación de strings
a = "uno"
b = "dos"
c = a + b # c es "unodos"
print("String:: c = a + b : " , c)
c = a * 3 # c es "unounouno"
print("String:: c = a * 3 : " , c)
#----------------------------------------------
# MÉTODOS DE LOS STRINGS:
# lower(): Convierte en minúsculas un string.
s_texto1 = "ESTE TEXTO ESTÁ INICIALMENTE EN MAYÚSCULAS"
print("String:: lower() : ", s_texto1.lower())

# capitalize(): Pone la primera letra en mayúscula.
s_texto2 = "este texto no tenía la primera letra en mayúsculas"
print("String:: capitalize() : ", s_texto2.capitalize())

# count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres.
s_texto3 = "Vamos a ver cuántas veces aparece la letra c"
print("String:: 'Vamos a ver cuántas veces aparece la letra c'.count('c') : ", s_texto3.count('c'))

# find(): Representa el índice o la posición en el cual aparece un carácter o un grupo de caracteres. Si aparece varias veces me dice sólo el primero.
s_texto4 = "Vamos a ver en qué posición aparece primero la letra e"
print("String:: 'Vamos a ver en qué posición aparece primero la letra e'.find('e') : ", s_texto4.find('e'))

# rfind(): Igual que find() pero contando desde atrás.
s_texto5 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print("String:: 'Vamos a ver en qué posición aparece la palabra desde, contando desde atrás'.find('desde') : ", s_texto5.rfind('desde'))

# isdigit(): Devuelve un boolean, nos dice si el valor introducido es un string. Tiene que ser un valor introducido entre comillas o dará error.
s_texto6 = "6"
print("String:: '6'.isdigit() : ", s_texto6.isdigit())

# isalum(): Devuelve un boolean, Devuelve verdadero si todos los caracteres de la cadena son alphanuméricos y hay al menos un carácter. En caso contrario, devuelve falso.
s_texto7 = "9857654gfz7"
print("String:: '9857654gf7'.isalnum() : ", s_texto7.isalnum())

# isalpha(): Devuelve un boolean, comprueba si hay sólo letras. Los espacios no cuentan.
s_texto8 = "Holamundo8"
print("String:: 'Holamundo8'.isalpha() : ", s_texto8.isalpha())

# split(): Separa por palabras utilizando espacios. Crea una lista.
s_texto9 = "Vamos a separar esta frase por los espacios"
print("String:: 'Vamos a separar esta frase por los espacios'.split() : ", s_texto9.split())

# Podemos usar otro carácter como separador, por ejemplo una coma:
s_texto10 = "Esta sería la primera parte,y esta la segunda"
print("String:: 'Esta sería la primera parte,y esta la segunda'.split(',') : ", s_texto10.split(","))

# strip(): Borra los espacios sobrantes al principio y al final.
s_texto11 = " En este texto había espacios al principio y al final "
print("String:: ' En este texto había espacios al principio y al final '.strip() : ", s_texto11.strip())

# replace(): Cambia una palabra o una letra por otra.
s_texto12 = "Vamos reemplazar la palabra casa"
print("String:: 'Vamos reemplazar la palabra casa'.replace('casa', 'hogar') : ", s_texto12.replace("casa", "hogar"))

# Te invito a que inspecciones el resto de funciones predefinidas para los strings en:
# https://www.freecodecamp.org/espanol/news/metodos-de-string-de-pythonexplicados-con-ejemplo/

# Salida directa de datos
Comon.titulo("Salida directa de datos")
print("print():: En esta ocasión hemos imprimido por pantalla este string")
# Salida de datos calculados
n_numero_1 = 4
n_numero_2 = 6
print("print()::El resultado de sumar" , n_numero_1, "y" , n_numero_2 , "es" , (n_numero_1+n_numero_2))
# Si concatenamos int y strings usando el signo + nos puede dar problemas.
#print("El resultado de sumar " + n_numero_1 + " y " + n_numero_2 + " es " + (n_numero_1+n_numero_2))

# Entrada directa de datos
Comon.titulo("Entrada directa de datos")

s_nombreIntroducido = "toto" #input("Introduzca su nombre: ")
print("inputf():: Bienvenido", s_nombreIntroducido)

# -------------------------------------
""" IMPORTANTE: Todo lo introducido por input() se considera string, aunque seaun número,
por lo que, si necesitamos operar matemáticamente con números, tendremos que hacer un casting:
"""
s_edad = int("46") #int(input("Introduzca su edad:"))
print("inputf():: El año que viene tendrá usted", s_edad + 1, "años")

# Operadores
Comon.titulo("Operadores")

# Módulo. Nos devuelve el resto de una división:
n_numerador = 85
n_denominador = 9
n_resto = n_numerador%n_denominador
print("Operadores :: módulo % : El resto de dividir" , n_numerador , "entre" , n_denominador , "es" , n_resto)

# == Igual que...
# No confundir con el operador de asignación =
# Con = le damos un valor a una variable. Con == comprobamos si dos objetos son iguales.
n_numero1 = 34
s_texto1 = "34"
print("Operadores :: n_numero1 == s_texto1 : ", n_numero1 == s_texto1)
n_numero2 = 34
n_numero3 = 34
print("Operadores :: n_numero2 == n_numero3 : ", n_numero2 == n_numero3)

# != Diferente que...
n_numero4 = 34
n_numero5 = 34
print("Operadores :: n_numero4 != n_numero5 : ", n_numero4 != n_numero5)

# += Suma e incremento
n_numero6 = 34
n_numero6 += 1 #Sería como poner:
print("Operadores :: n_numero6 += 1 : ", n_numero6)
n_numero6 = n_numero6 +1
print("Operadores :: n_numero6 = n_numero6 + 1 : ", n_numero6)

# Operadores lógicos
Comon.titulo("Operadores lógicos")

a = True
b = False
resultado = a and b
print("Operadores lógicos :: a and b : ", resultado)
resultado = a or b
print("Operadores lógicos :: a or b : ", resultado)
resultado = not a
print("Operadores lógicos :: not a : ", resultado)
#----------------------------------
# Sintaxis simplificada para varios operadores lógicos
edad = 35 #int(input('Introduce tu edad: '))
veintes = edad >= 20 and edad < 30
print("Operadores lógicos :: veintes : ", veintes)
treintas = edad >= 30 and edad <40
print("Operadores lógicos :: treintas : ", treintas)

if ( 20 <= edad < 30) or (30 <= edad <40):
    print('Operadores lógicos :: Dentro de rango (20\'s) o (30\'s)')

    if veintes:
        print('Operadores lógicos :: Dentro de los 20\'s')
    elif treintas:
        print('Operadores lógicos :: Dentro de los 30\'s')
    else:
        print('Operadores lógicos :: Fuera de rango')
else:
    print("Operadores lógicos :: No está dentro de los 20's ni 30's")

# Dirección de memoria
Comon.titulo("Dirección de memoria")

# Obtener la dirección de memoria de una variable
a = 65
print("Dirección de memoria :: id(a) - a = 65 :" , id(a))
# Obtener la dirección de memoria de una variable que apunta a otra
miNumero = 65
miNumero2 = miNumero
print("Dirección de memoria :: id(miNumero) - miNumero = 65 :" , id(miNumero))
print("Dirección de memoria :: id(miNumero2) - miNumero2 = miNumero) :" , id(miNumero2))
# Si cambio la variable, realmente creo una copia en otra dirección de memoria:
a = 65
print("Dirección de memoria :: id(a) - a = 65:" , id(a))
a+=2
print("Dirección de memoria :: id(a) - a+=2 :" , id(a))

# Obtener la dirección de memoria de una tupla
a = (1, 2, 3, 4, 5)
print("Dirección de memoria :: id(a) - tupla :" , id(a))

# Obtener la dirección de memoria de una lista
a = [1, 2, 3, 4, 5]
print("Dirección de memoria :: id(a) - lista :" , id(a))
# Obtener la dirección de memoria de un diccionario
a = {'a': 1, 'b': 2}
print("Dirección de memoria :: a :", a)
print("Dirección de memoria :: id(a) - dicionario :" , id(a))
a["c"] = 3
print("Dirección de memoria :: a['c'] = 3 :", a)
print("Dirección de memoria :: id(a) - dicionario :" , id(a))