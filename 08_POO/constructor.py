# Creación de la clase Coche
class Coche():
    # Declaración del constructor de la clase Coche
    def __init__(self):
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False
    # Declaración de métodos
    def arrancar(self): #self hace referencia a la instancia de clase.
        self.is_enMarcha = True #Es como si pusiésemos miCoche.is_enMarcha = True
    def estado(self):
        if (self.is_enMarcha):
            return "El coche está arrancado"
        else:
            return "El coche está parado"

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
coche_1 = Coche()
# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
coche_1.ruedas = 7
print("El largo del coche es de" , coche_1.largo, "cm.")
coche_1.arrancar()
print(coche_1.estado())
# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche está arrancado:" ,
coche_1.arrancar()) 

class Camion:
    # Declaración del constructor con parámetros
    def __init__(self, largo, ancho, ruedas, peso, color, is_enMarcha):
        self.ancho = ancho
        self.ruedas = ruedas
        self.peso = peso
        self.color = color
        self.is_enMarcha = is_enMarcha
# Declaración de dos instancias de clase pasándoles los parámetros requeridos en el constructor.
camion_1 = Camion(400, 160, 4, 1200, "amarillo", True)
camion_2 = Camion(420, 150, 4, 1500, "verde", False)

class Book():
    """
    Clase para trabajar con libros
    """
    def __init__(self, title, author = "", electronic = False):
        self.title = title
        self.author = author
        self.is_electronic = electronic
    def __del__(self):
        print("Acabas de llamar al método destructor. El objeto acaba de ser eliminado")


libro = Book("Lazarillo de Tormes")
libro.title
del libro
   