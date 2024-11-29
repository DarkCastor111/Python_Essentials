import Comon
import copy

Comon.titulo("Listas por comprension")

miLista1 = [1,2,3,4,5,6,7,8,9]
miLista1 = [n for n in range(10)]
print("miLista1 = ", miLista1)

miLista1 = [n**2 for n in range(10)]
print("miLista1 = ", miLista1)

miLista2 = [2 * elemento for elemento in miLista1]
print("miLista2 = [2 * elemento for elemento in miLista1] : ", miLista2)

miListaPares = [elemento for elemento in miLista1 if elemento%2==0]
print("miListaPares = [elemento for elemento in miLista1 if elemento%2==0] : ", miListaPares)

miListaA = ["a", "b", "c"]
miListaB = [1, 2, 3]
miListaC = [elemento1 * elemento2 for elemento1 in miListaA for elemento2 in miListaB]
print("miListaC = miListaA '*' miListaB : ", miListaC)

matrizM = [["a1","a2","a3"],["b1","b2","b3"],["c1","c2","c3"]]
print("matrizM = ", matrizM)
miListaCol = [row[0] for row in matrizM]
print("miListaCol = ", miListaCol)
miListaRow = matrizM[0]
print("miListaRow = ", miListaRow)
miListaDiag = [matrizM[i][i] for i in [0,1,2]]
print("miListaDiag = ", miListaDiag)

Comon.titulo("Copiar una lista")
list_a = [1, 2, 3]
list_aa = list_a        # NO es una copia (objeto mutable)
list_b = list_a[:]      # Copiamos la lista
list_c = list(list_a)   # Otra manera
list_a[2] = 'z'         # Cambiamos la list_a

print("list_a = ", list_a)
print("list_aa = ", list_aa)
print("list_b = ", list_b)
print("list_c = ", list_c)

Comon.titulo("modulo copy")

lisCopyA = [1,2, [31,32,33]]
lisCopyB = copy.copy(lisCopyA)      # Copia solo un nivel => el resto sigue compartido
lisCopyC = copy.deepcopy(lisCopyA)  # Copia todos los niveles

lisCopyA[1] = 'z'
lisCopyA[2][2] = 'zz'

print("lisCopyA = ", lisCopyA)
print("lisCopyB (copy.copy(lisCopyA)) : ", lisCopyB)
print("lisCopyC (copy.deepcopy(lisCopyA)) : ", lisCopyC)


