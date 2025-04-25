from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    SELECCIONAR_TODOS = 'SELECT * FROM cliente ORDER BY id'
    SELECCIONAR_UNO = 'SELECT * FROM cliente where id=%s'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    CREAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar_todos(cls):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            cur.execute(cls.SELECCIONAR_TODOS)
            lineas = cur.fetchall()
            print(f'==> {cur.rowcount} cliente(s) encontrado(s)')
            # Mapeo clase-tabla cliente
            clientes = []
            for linea in lineas:
                cli = Cliente(linea[0],
                                  linea[1],
                                  linea[2],
                                  linea[3]
                                  )
                clientes.append(cli)
            return clientes
        except Exception as e:
            print(f'Ocurrio un error al seleccionar clientes : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)

    @classmethod
    def seleccionar_uno_con_id(cls, id_cliente):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            valores = (id_cliente,)
            cur.execute(cls.SELECCIONAR_UNO, valores)
            linea = cur.fetchone()
            # Mapeo clase-tabla cliente
            cliente_encontrado = Cliente(   linea[0], linea[1],
                                            linea[2], linea[3] )
            print(f'{cur.rowcount} cliente encontrado : {cliente_encontrado}')
            return cliente_encontrado
        except Exception as e:
            print(f'Ocurrio un error al seleccionar un cliente por id : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)


    @classmethod
    def crear(cls, cliente):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            valores =(cliente.nombre, cliente.apellido, cliente.membresia)
            cur.execute(cls.CREAR, valores)
            con.commit()
            print(f'==> Cliente {cliente} añadido correctamente!')
            return cur.rowcount

        except Exception as e:
            print(f'Error al gardar un nuevo cliente : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)

    @classmethod
    def actualizar(cls, cliente):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            valores =(cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cur.execute(cls.ACTUALIZAR, valores)
            con.commit()
            print(f'==> Cliente {cliente} actualizado correctamente!')
            return cur.rowcount
        except Exception as e :
            print(f'Error a actualizar el cliente {cliente} : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)
    
    @classmethod
    def eliminar_uno(cls, cliente):
        con = None
        try:
            con = Conexion.obtener_conexion()
            cur = con.cursor()
            valores =(cliente.id,)
            cur.execute(cls.ELIMINAR, valores)
            con.commit()
            print(f'==> Cliente #{cliente.id} eliminado correctamente!')
            return cur.rowcount
        except Exception as e :
            print(f'Error a eliminar el cliente #{cliente.id} : {e}')
        finally:
            if con is not None:
                cur.close()
                Conexion.liberar_conexion(con)




# Prueba
if __name__ == "__main__":
    '''
    # Insertar un nuevo cliente
    cli1 = Cliente(p_nombre='Peter', p_apellido='Parker', p_membresia='350')
    result1 = ClienteDAO.crear(cli1)
    print(f'{result1} cliente insertado : {cli1}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar_todos()
    for cliente in clientes:
        print(cliente)

    # Actualizar un cliente
    cli2_actualizado = Cliente(5, 'Bruce', 'Wayne', 250)
    result2 = ClienteDAO.actualizar(cli2_actualizado)
    print(f'{result2} cliente actualizado : {cli2_actualizado}')

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar_todos()
    for cliente in clientes:
        print(cliente)

    # Eliminar el cliente 3
    cli3 = Cliente(p_id = 3)
    result3 = ClienteDAO.eliminar_uno(cli3)
    print(f'{result3} cliente(s) eliminado(s)')
    '''

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar_todos()
    for cliente in clientes:
        print(cliente)


