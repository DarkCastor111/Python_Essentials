def mon_decorateur(fonction):
    def fonction_modifiee(*args, **kwargs):
        print("Avant exécution...")
        fonction(*args, **kwargs)
        print("Après exécution !")
    return fonction_modifiee

@mon_decorateur
def dire_bonjour(nombre):
    print(f"Bonjour {nombre}!")

# Appel de la fonction
print("### Decoradores en Python")
dire_bonjour("Christophe")


print("### Exemple : Calcul de durée d'exécution")

import time

def chronometre(fonction):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = fonction(*args, **kwargs)
        fin = time.time()
        print(f"Temps d'exécution : {fin - debut:.4f} secondes")
        return resultat
    return wrapper

@chronometre
def somme(n):
    # time.sleep(1)  # Simule un calcul long
    return sum(range(n))

print(somme(1000000))
