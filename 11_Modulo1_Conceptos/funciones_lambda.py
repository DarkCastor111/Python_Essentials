print("### Funciones Lambda")

# Funcion cuadrado sin usar lambda
def cuadrado(x):
    return x ** 2

# Funcion lambda (anonima)
cuadrado_lambda = lambda x: x** 2


valor=5
print(f"El cuadrado de {valor}: {cuadrado(valor)}")
print(f"El cuadrado lambda de {valor}: {cuadrado_lambda(valor)}")

print()
print("### Lambda con map()")

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
squared_numbers_lambda = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # [1, 4, 9, 16, 25]
print(squared_numbers_lambda)  # [1, 4, 9, 16, 25]

print()
print("### Lambda con sort()")

def sort_by_second(pair):
    return pair[1]

pairs = [(1, 3), (2, 2), (4, 1)]
sorted_pairs = sorted(pairs, key=sort_by_second)
sorted_pairs_lambda = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # [(4, 1), (2, 2), (1, 3)]
print(sorted_pairs_lambda)  # [(4, 1), (2, 2), (1, 3)]

print()
print("### Lambda con filter()")

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(is_even, numbers))
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # [2, 4, 6]
print(even_numbers_lambda)  # [2, 4, 6]
