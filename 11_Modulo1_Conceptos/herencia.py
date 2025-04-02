class Animal:
    def comer(self):
        print('Como muchas veces al día')

    def dormir(self):
        print('Duermo muchas horas')

    def hacer_sonido(self):
        print('Sonido de animal no conocido')

class Perro(Animal): # Herencia
    def hacer_sonido(self):
        print('Wuaf Wuaf')

    def dormir(self): # Sobreescritura
        print('Duermo 15 horas al día')

class Gato(Animal): # Herencia
    def hacer_sonido(self):
        print('Miaow')


def que_sonido_hace(animal): # Función polimórfica
    animal.hacer_sonido()

print('### Ejemplo de Herencia en Python')
print('### Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
animal1.hacer_sonido()

print()
print('### Perro(Animal)')
perro1 = Perro()
perro1.comer()
perro1.dormir()
perro1.hacer_sonido()

print()
print('### Polimorfismo con herencia')

import math

class Forme:
    def aire(self):
        raise NotImplementedError("Cette méthode doit être implémentée dans une sous-classe")

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    
    def aire(self):
        return math.pi * self.rayon ** 2

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

def afficher_aire(figure): # Fonction polymorphique
    print(f"Aire : {figure.aire()}")

# Test
c = Cercle(5)
r = Rectangle(4, 6)

print('afficher_aire(c) : ')
afficher_aire(c)  # Aire : 78.54
print('afficher_aire(r) : ')
afficher_aire(r)  # Aire : 24


print()
print('### Polimorfismo sin herencia')
class Chien:
    def parler(self):
        return "Woof!"

class Chat:
    def parler(self):
        return "Miaou!"

# Fonction polymorphique
def faire_parler(animal):
    print(animal.parler())

# Test
chien = Chien()
chat = Chat()
print('faire_parler(chien) : ')
faire_parler(chien)  # Woof!
print('faire_parler(chat) : ')
faire_parler(chat)    # Miaou!

print()
print('### Polimorfismo con métodos integrados')

print('len("Python") :')
print(len("Python"))   # 6 (Chaîne de caractères)
print('len([1, 2, 3]) :')
print(len([1, 2, 3]))  # 3 (Liste)
print('len({"a": 1, "b": 2}) :')
print(len({"a": 1, "b": 2}))  # 2 (Dictionnaire)
