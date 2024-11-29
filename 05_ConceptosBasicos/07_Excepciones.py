capitulo = 0

def titulo(_tit):
    global capitulo
    capitulo += 1
    print()
    print("#####################################")
    print("##", capitulo, "##  " + _tit)
    print("#####################################")

# Definición de una excepción - class :
class miPropiaExcepcion(Exception): #Las excepciones heredan de Exception
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)

titulo("funcion indexador")

def indexador(objeto, indice):
    return objeto[indice]

print("+ pos 0 de 'Python' = ", indexador('Python', 0))

titulo("Try, Except")

# try, except
try:
    indexador('Python', "10")
except (IndexError): # Captura IndexError
    # except: # Captura todos los errores - no recomendado
    print('Has puesto un índice muy grande o algo que no sea un indice.')
except (TypeError): # Captura TypeError
    print('Has puesto algo que no sea un indice.')

print('Hemos salido del try-catch')
print()

titulo("Raise")
# raise
try :
    raise IndexError('Excepción lanzada manualmente')
except (IndexError): # Captura IndexError
    print('Has capturado tu propia excepción')

print('Hemos salido del try-catch')
print()

titulo("Assert")
# assert (no recomendado en producción)
a = 10
b = 0
assert(a > b), 'A tiene que ser mayor que B' # Si se cumple no salta el AssertionError
print('Si se muestra esto es que no ha saltado el assert')
print()

titulo("Creando excepciones")
# Creando excepciones
try:
    raise miPropiaExcepcion("Mensaje1")
except miPropiaExcepcion:
    print('He capturado una miPropiaExcepcion : ', miPropiaExcepcion)
print()
# raise(miPropiaExcepcion('Mensaje Error : Mensaje especifico'))

titulo("finally")
# finally
try:
    indexador('Python', 5)
    print('****Esto no se ejecuta cuando salta la excepción')
finally:
    print('Esto se ejecuta includo cuando salta la excepción o no')
print('****Esto no se ejecuta cuando salta la excepción')

titulo("else")
# else

def divide(x, y):
    try:
        resultado = x/y
        print('No hay excepción')
    except ZeroDivisionError:
        print('No se puede dividir por cero')
    else:
        print('El resultado es: ', resultado)
    finally:
        print('Ejecutamos el finally')

print()
print("Excepciones de la funcion divide")
divide(4, 12)
print()
divide(4, 0)