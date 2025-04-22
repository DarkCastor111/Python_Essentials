class Producto:
    def __init__(self, p_nombre, p_cantidad, p_precio, p_categoria):
        self.nombre = p_nombre
        self.cantidad = int(p_cantidad)
        self.precio = float(p_precio)
        self.categoria = p_categoria

    def __str__(self):
        return f'{self.nombre} ({self.categoria}) : {self.cantidad} - {self.precio:.2f} Euros'
    
# Prueba
if __name__ == "__main__":
    prod1 = Producto("Produit1", 5, 3.14, "Fruits")
    print(prod1)