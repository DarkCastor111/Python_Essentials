import Comon


Comon.titulo("Herencia")
class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True

    def arrancar(self):
        self.arrancado = True
        self.parado = False

    def parar(self):
        self.parado = True
        self.arrancado = False

    def resumen(self):
        print("\n Marca:", self.marca, "\n",
        "Modelo:", self.modelo, "\n",
        "Color:", self.color, "\n",
        "Está arrancado:", self.arrancado,"\n",
        "Está parado:", self.parado )

Comon.parte("Herencia : coche = Vehiculo")
miCoche = Vehiculo("Renault", "Megane")
miCoche.arrancar()
miCoche.resumen()

Comon.parte("Herencia : Moto(Vehiculo)")
class Moto(Vehiculo):
    is_carenado = False

    #Método propio de la clase Moto, no heredado del padre.
    def poner_carenado(self):
        self.is_carenado = True
    #La clase Moto sobrescribe el método resumen() heredado del padre
    def resumen(self):
        print(" El modelo es una moto", "\n",
        "Marca:", self.marca, "\n",
        "Modelo:", self.modelo, "\n",
        "Color:", self.color, "\n",
        "Está arrancado:", self.arrancado,"\n",
        "Está parado:", self.parado, "\n",
        "Tiene carenado:", self.is_carenado)

miMoto = Moto("Kawasaki", "Ninja")
miMoto.resumen()

Comon.parte("Herencia : Kwad(Moto)")
class Kwad(Moto):
    pass

miKwad = Kwad("Linhai", "LH 500")
miKwad.resumen()

Comon.parte("super()")
class Persona():
    def __init__(self, nombre, edad, lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar
    def descripcion(self):
        print("\n El nombre es ", self.nombre, ", tiene ", self.edad, " anyos", " y es de ", self.lugar)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, lugar_epm):
        super().__init__(nombre_emp, edad_emp, lugar_epm)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print(" Salario: ", self.salario, ", antiguedad: ", self.antiguedad)

Angel=Persona("Angel", 43, "Malaga")
Angel.descripcion()

Empleado1=Empleado(2000, 2017, "Manolo", 33, "Madrid")
Empleado1.descripcion()

Comon.parte("sin super()")
class Padre(): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
        #Definimos los Atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas

class Hijo1(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el constructor
        self.ojos = ojos #Sobreescribimos cada atributo
        self.cejas = cejas
        self.cara = cara #Especificamos el nuevo atributo para Hijo


tomas = Hijo1('Marrones', 'Negras', 'Larga') #Instanciamos
print ("Tomas = ", tomas.ojos, tomas.cejas, tomas.cara) #Imprimimos los atributos del objeto

Comon.parte("super() : con llamada a la superclase")
class Hijo2(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        Padre.__init__(self, ojos, cejas)
        #Especificamos la clase y llamamos a su constructor + Atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo

tomas2 = Hijo2('Marrones', 'Negras', 'Larga')
print ("Tomas2 = ", tomas2.ojos, tomas2.cejas, tomas2.cara)

Comon.titulo("Encapsulación")

class Ejemplo:
    __atributo_privado = "atributo inalcanzable desde fuera."
    def __metodo_privado(self):
        print("método inalcanzable desde fuera.")
    def atributo_publico(self):
        return "El atributo es=", self.__atributo_privado
    def metodo_publico(self):
        print("El método privado es: ", end="")
        return self.__metodo_privado()

Comon.parte("Ejemplo")
e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()

class CocheEncaps:
    # Método constructor
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False
    # Declaración de métodos
    def arrancar(self): # self hace referencia a la instancia de clase.
        self.is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha = True
    def estado(self):
        if (self.is_enMarcha):
           return "El coche está arrancado"
        else:
           return "El coche está parado"

Comon.parte("Ejemplo2") # Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche2 = CocheEncaps()
miCoche2.__ruedas = 9 #Aunque hay el simbolo __, se puede cambiar
print("Mi coche tiene", miCoche2.__ruedas, "ruedas.")
miCoche2.arrancar()
print(miCoche2.estado())

Comon.titulo("Polimorfismo")

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    def __str__(self):
        return f'Empleado: [Nombre:{self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento:{self.departamento}] {super().__str__()}'

def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())


empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)
gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)