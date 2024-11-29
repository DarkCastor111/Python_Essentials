import Comon


Comon.titulo("Tuplas")

# Definicion
tup1 = (8,)
print("type(tup1) = ", type(tup1))

tup2 = 1,2,3,4
print("tup2 : ", tup2)
print("type(tup2) = ", type(tup2))
num1, num2, num3, num4 = tup2
print("num1, num2, num3, num4 : ", num1, num2, num3, num4, sep=" | ")