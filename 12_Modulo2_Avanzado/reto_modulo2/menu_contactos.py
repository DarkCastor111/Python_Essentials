from gestion_contactos import GestionContactos

def mostrar_menu():
    print("\n--- Menú de Gestión de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos los contactos")
    print("5. Salir")


    
def main():
    gestion = GestionContactos()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre del contacto: ")
            telefono = input("Teléfono del contacto: ")
            email = input("Email del contacto: ")
            gestion.anadir_contacto(nombre, telefono, email)
        
        elif opcion == "2":
            nombre = input("Nombre o parte de nombre del contacto a buscar: ")
            gestion.buscar_contacto(nombre)
        
        elif opcion == "3":
            email = input("Email del contacto a eliminar: ")
            gestion.eliminar_contacto(email)
        
        elif opcion == "4":
            gestion.mostrar_contactos() 
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()