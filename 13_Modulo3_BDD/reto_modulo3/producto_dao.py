from conexion import Conexion
from producto import Producto
from mysql.connector import IntegrityError

class ProductoDAO:
    SELECCIONAR_TODOS = 'SELECT * FROM producto ORDER BY nombre'
    SELECCIONAR_UNO_POR_NOMBRE = 'SELECT * FROM producto where nombre like %s'
    ACTUALIZAR_PRECIO_CANTIDAD = 'UPDATE producto SET precio=%s, cantidad=%s WHERE nombre=%s'
    CREAR = 'INSERT INTO producto(nombre, categoria, precio, cantidad) VALUES (%s, %s, %s, %s)'
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

    @classmethod
    def seleccionar_con_nombre(cls, nombre):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            cur.execute(cls.SELECCIONAR_UNO_POR_NOMBRE, (f'%{nombre}%',))
            lineas = cur.fetchall()
            print(f'==> {cur.rowcount} producto(s) encontrado(s)')
            productos = []
            for linea in lineas:
                productos.append(Producto(p_nombre = linea[0], p_cantidad = linea[1], p_precio = linea[2], p_categoria = linea[3]))
            return productos

        except Exception as e:
            print(f'Ocurrio un error al seleccionar productos con el nombre {nombre} : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)
    
    @classmethod
    def crear(cls, prd):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            cur.execute(cls.CREAR, (prd.nombre, prd.categoria, prd.precio, prd.cantidad))
            con.commit()
            print(f'==> {prd} añadido correctamente')
            return cur.rowcount

        except IntegrityError as ie:
            print(f'Ya existe un producto con el mismo nombre : {prd.nombre}')   
        except Exception as e:
            print(f'Ocurrio un error a la creación del producto {prd} : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)

    @classmethod
    def actualizar(cls, prd):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            cur.execute(cls.ACTUALIZAR_PRECIO_CANTIDAD, (prd.precio, prd.cantidad, prd.nombre))
            con.commit()
            if cur.rowcount == 1:
                print(f'==> {prd.nombre} actualizado correctamente')
            else:
                print(f'==> {cur.rowcount} productos actualizados !!')
            return cur.rowcount

        except Exception as e:
            print(f'Ocurrio un error a la actualización del producto {prd} : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)

    @classmethod
    def eliminar_uno(cls, nmb):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            cur.execute(cls.ELIMINAR, (nmb, ))
            con.commit()
            if cur.rowcount != 1:
                print(f'==> {nmb} no encontrado')
            else:
                print(f'==> {nmb} eliminado correctamente')
        except Exception as e:
            print(f'Ocurrio un error a la eliminación del producto {nmb} : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)



