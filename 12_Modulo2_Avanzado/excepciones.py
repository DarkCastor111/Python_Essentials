print('### Manejo de excepciones')

def dividir(numerador, denominador):
    try:
        # Revisamos si el denominador es STOP
        if denominador == "STOP":
            raise Exception('STOP recibido')
        resultado = numerador / denominador
        print(f'El resultado de {numerador} / {denominador} es {resultado}')
    except ZeroDivisionError:
        print(f'Error : No se puede dividir entre cero')
    except TypeError:
        print(f'Error : Proporcionar valores numericas')
    except Exception as e:
        print(f'Error : Ocurrió un error : {e}')
    else:
        print('No ocurrió ningún error')
    finally:
        print(f'Terminamos de procesar\n')



#Ejemplo de uso
dividir(8, 4)
dividir(8, 0)
dividir("a", 2)
dividir("a", "STOP")