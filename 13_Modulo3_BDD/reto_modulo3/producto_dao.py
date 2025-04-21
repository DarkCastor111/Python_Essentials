from conexion import Conexion
from producto import Producto

class ProductoDAO:
    SELECCIONAR_TODOS = 'SELECT * FROM producto ORDER BY nombre'
    SELECCIONAR_UNO_POR_NOMBRE = 'SELECT * FROM producto where nombre=%s'
    ACTUALIZAR_PRECIO_CANTIDAD = 'UPDATE producto SET precio=%s, cantidad=%s WHERE nombre=%s'
    CREAR = 'INSERT INTO producto(nombre, categoria, precio, cantidad) VALUES (%s, %s, %s)'
    ELIMINAR = 'DELETE FROM producto WHERE nombre=%s'

    @classmethod
    def seleccionar_todos(cls):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            cur.execute(cls.SELECCIONAR_TODOS)
            lineas = cur.fetchall()
            print(f'==> {cur.rowcount} producto(s) encontrados')
            productos = []
            for linea in lineas:
                productos.append(Producto(p_nombre = linea[0], p_cantidad = linea[1], p_precio = linea[2], p_categoria = linea[3]))
            return productos

        except Exception as e:
            print(f'Ocurrio un error al seleccionar productos : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)


