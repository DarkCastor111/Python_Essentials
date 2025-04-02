class Producto():
    # Constructor con valores por defecto
    def __init__(self, nbr = "por defecto", ctg= "no categoria", prc= 10.0, ctd = 1):
        self.__nombre = nbr
        self.__categoria = ctg
        self.__precio = prc
        self.__cantidad = ctd
       
    # Para poder escribir print(miProducto)
    def __str__(self):
        return "Nombre(Categoria): {}({}) | Precio: {} | Cantidad: {}".format(self.__nombre, self.__categoria, self.__precio,self.__cantidad)

    # Getters
    def get_nombre(self):
        return self.__nombre
    def get_categoria(self):
        return self.__categoria
    def get_precio(self):
        return self.__precio
    def get_cantidad(self):
        return self.__cantidad

    # Setters
    # Los setters  contienen las validaciones  
    def set_nombre(self, nbr):
        if nbr == "":
            print("XXX ERROR: El nombre no puede ser vacío.")
            return False
        else:
            self.__nombre = nbr
            return True

    def set_categoria(self, ctg):
        if ctg == "":
            print("XXX ERROR: La categoria no puede ser vacía.")
            return False
        else:
            self.__categoria = ctg
            return True

    def set_precio(self, prc):
        try:
            precio = float(prc)
        except Exception:
            print("XXX ERROR: El precio no es correcto.")
            return False
        if precio > 0:
            self.__precio = precio
            return True
        else:
            print("XXX ERROR: El precio debe ser siempre mayor que 0.")
            return False

    def set_cantidad(self, ctd):
        try:
            cantidad = int(ctd)
        except Exception:
            print("XXX ERROR: La cantidad no es correcta.")
            return False
        if cantidad >= 0:
            self.__cantidad = ctd
            return True
        else:
            print("XXX ERROR: La cantidad debe ser mayor o igual que 0.")
            return False

    def modificarProducto(self):
        while not(self.set_precio(input("- Nuevo Precio: "))):
            pass
        while not(self.set_cantidad(input("- Nueva Cantidad: "))):
            pass

    def nuevoProducto(self):
        print("\nNuevo producto :")
        while not(self.set_nombre(input("- Nombre: "))):
            pass
        while not(self.set_categoria(input("- Categoria: "))):
            pass
        while not(self.set_precio(input("- Precio: "))):
            pass
        while not(self.set_cantidad(input("- Cantidad: "))):
            pass

class Inventario():
    # Constructor
    def __init__(self):
        self.__productos = []

        # Inventario inicial para agilizar los tests
        """
        prod1 = Producto("Piña", "Fruta", 2.5, 25)
        prod2 = Producto("Papa", "Verdura", 1, 20)
        prod3 = Producto("Plátano", "Fruta", 2, 15)
        self.__productos.append(prod1)
        self.__productos.append(prod2)
        self.__productos.append(prod3)
        """

    # Getters
    def get_productos(self):
        return self.__productos

    # Setters
    def set_productos(self, listaProductos):
        self.__productos = listaProductos
    # Para modificar solo un producto en la lista (no utlizada)
    def set_producto(self, producto, i):
        self.__productos[i] = producto
    # Para agregar un nuevo producto
    def add_producto(self, productoAAnadir):
        resultadoBusqueda = self._find_productoConNombre(productoAAnadir.get_nombre())
        if resultadoBusqueda[0]:
            print("==> ALERTA : Producto ya existente.")
        else:
            self.__productos.append(productoAAnadir)
            print("--> INFO : Producto {} añadido.".format(productoAAnadir.get_nombre()))

    # Método de búsqueda interna utilizada dentro de la mayoría de las operaciones
    # La salida es un tuple que contiene :
    # resultado[0] un booleano, True si se ha encontrado un producto 
    # resultado[1] el Producto encontrado, 
    # resultado[2] su posición en el inventario
    def _find_productoConNombre(self, nombreProducto):            
        i = 0
        for pr in self.__productos:
            if pr.get_nombre() == nombreProducto:
                return (True, pr, i)
            i += 1
        return (False, "", i)

    def agregarProducto(self):
        print("\n## Agregar producto ##")
        # Creación
        productoAAgregar = Producto()
        productoAAgregar.nuevoProducto()
        # Agregación al inventario
        self.add_producto(productoAAgregar)

    def eliminarProducto(self):
        print("\n## Eliminar producto ##")
        nombreProductoAEliminar = input("Nombre del producto a eliminar: ")

        resultadoBusqueda = self._find_productoConNombre(nombreProductoAEliminar)
        if resultadoBusqueda[0]:
            self.__productos.remove(self.__productos[resultadoBusqueda[2]])
            print("--> INFO : Producto {} eliminado correctamente.".format(nombreProductoAEliminar))
        else:
            print("==> ALERTA : Producto {} no encontrado.".format(nombreProductoAEliminar))

    def buscarProducto(self):
        print("\n## Buscar producto ##")
        nombreProductoABuscar = input("Nombre del producto a buscar: ")

        resultadoBusqueda = self._find_productoConNombre(nombreProductoABuscar)
        if resultadoBusqueda[0]:
            print("--> INFO : Producto {} encontrado.".format(nombreProductoABuscar))
            print(resultadoBusqueda[1])
        else:
            print("==> ALERTA : Producto no encontrado.")

    def actualizarProducto(self):
        print("\n## Actualizar producto ##")
        nombreProductoAActualizar = input("Nombre del producto a actualizar: ")

        resultadoBusqueda = self._find_productoConNombre(nombreProductoAActualizar)
        if resultadoBusqueda[0]:
            print("--> INFO : Producto {} encontrado.".format(nombreProductoAActualizar))
            print(resultadoBusqueda[1])
            # Modificamos el producto encontrado
            # Lo "mágico" es que es _El_ Producto dentro del Inventario
            resultadoBusqueda[1].modificarProducto()
            print("--> INFO : Producto {} actualizado correctamente.".format(nombreProductoAActualizar))
        else:
            print("==> ALERTA : Producto no encontrado.")
       
    def mostrarInventario(self):
        print("\n## Mostrar Inventario ##")
        if  len(self.__productos) == 0 :
            print("==> ALERTA : Inventario vacío.")
        i=0
        for prd in self.__productos:
            i += 1
            print("# Producto {} : {}".format(i,prd))

 
def printMenuPrincipal():
    print("\n## MENU PRINCIPAL ##")
    print(" 1. Agregar un producto...")
    print(" 2. Actualizar un producto...")
    print(" 3. Eliminar un producto...")
    print(" 4. Mostrar inventario.")
    print(" 5. Buscar un producto...")
    print(" 6. Salir =>")

print("\n###############################")
print("##   GESTION DE INVENTARIO   ##")
print("###############################")

salir = False
inventario = Inventario()
printMenuPrincipal()

while not salir:
    operacionCorrecta=False
    operacion = 0
    while not operacionCorrecta:
        seleccion = input("\nSelecciona una operación: ")
        try:
            operacion = int(seleccion)
        except Exception:
            print("XXX ERROR : Operación incorrecta.")
            printMenuPrincipal()
            continue
        if not 7 > operacion > 0:
            print("XXX ERROR : Operación incorrecta.")
            printMenuPrincipal()
        else:
            operacionCorrecta = True

    if operacion == 1:
        inventario.agregarProducto()
    elif operacion == 2:
        inventario.actualizarProducto()
    elif operacion == 3:
        inventario.eliminarProducto()
    elif operacion == 4:
        inventario.mostrarInventario()
    elif operacion == 5:
        inventario.buscarProducto()
    if operacion == 6:
        salir = True

