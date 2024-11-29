import Comon
from random import shuffle

Comon.titulo("Mínimo de dos números.")
def minimum(a, b) :
    return a if a < b else b

print(minimum(4, 2))

Comon.titulo("Invertir palabras de una cadena.")
def rev_frase(frase):
    palabras = frase.split(' ')
    frase_inv = '|'.join(reversed(palabras))
    return frase_inv

print(rev_frase("geeks quiz practice code"))

Comon.titulo("Suma de los elementos de una tupla.")
tup1 = (7, 8, 9, 1, 10, 7)
print("tupla original = ", str(tup1))
lis1 = list(tup1)
print("tupla en list = ", str(lis1))
res = sum(lis1) # conviertiendo una tupla en una lista
print("suma = ", res)

Comon.titulo("Calculo de una lista de números - recursivo")
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
    
print("suma (con list_sum)= ", list_sum(list(tup1)))

Comon.titulo("Desordene al azar una lista.")
x = ["Skyrim", "Pertenece", "A", "Los", "Nórdicos"]
shuffle(x)
print("x desordenada : ", x)

Comon.titulo("Caracteres en mayuscula.")
texto = "Contar las caractereS en mayusculas de uN texto"
count = 0
for caracter in texto:
    if caracter.isupper():
        count +=1
print(texto, ":", count)

Comon.titulo("Convertir un listado de string en número")
lis6 = ["1", "8", "4", "0", "3"]
print("lis6 = ", lis6)
lis6_num = [int(i) for i in lis6]
print("lis6_num =", lis6_num)
lis6_num.sort()
print("lis6_num ordenada =", lis6_num)

Comon.titulo("Valor de lista[-1]")
print("lis6_num =", lis6_num)
print("lis6_num[-1] =", lis6_num[-1])

Comon.titulo("Fibonacci")
# n_string = input("Introduzca el numero de valores de 'n' : ")
# n = int(n_string)
n = 10
first, second = 0, 1
sum = 0
count = 1
print("Secuencia de Fibonacci: ")
while (count <= n):
    print(sum)
    count += 1
    first = second
    second = sum
    sum = first + second

Comon.titulo("Numero primo")
def isPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

result = isPrimo(113)
if result:
    print("El numero es primo!!")
else:
    print("El numero NO es primo!!")

Comon.titulo("Nombres reflejos")
texto="LAVALO"
otxet=texto[::-1] # imagen reflejo de la lista
if texto == otxet:
    print("{} es capicúa".format(texto))
else:
    print("{} y {} no son iguales.".format(texto, otxet))

Comon.titulo("Declaraciones")
a,b,c = 5,5,5
print("a,b,c = 5,5,5 => a={}, b={}, c={}".format(a,b,c))

abc = 1000.000
print("abc = 1000.000 => abc = ", abc)
a,b,c = 1000,2000,3000
print("a,b,c = 1000,2000,3000 => a={}, b={}, c={}".format(a,b,c))
a,b,c = 1,000,000
print("a,b,c = 1,000,000 => a={}, b={}, c={}".format(a,b,c))
a_b_c= 1000,000,000 # Tuple
print("a_b_c= 1000,000,000 => a_b_c = ", a_b_c)

Comon.titulo("Excepciones")
try:
    if '1' != 1:
        raise "algún error"
    else:
        print("no se ha producido algún error")
except "algún error":
    print ("se ha producido algún error")




