from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    PUERTO = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: #Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POOL_SIZE,
                    host = cls.HOST,
                    port = cls.PUERTO,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool : {e}')
        else:
            return cls.pool
        
    @classmethod
    def obtener_conexion(cls):
        try:
            return cls.obtener_pool().get_connection()
        except Error as e:
            print(f'Ocurrio un error al obtener la conexión : {e}')
        return None

       
    
    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


# Prueba
if __name__ == "__main__":
    # Creación objeto pool
    pool_test = Conexion.obtener_pool()
    print(pool_test)
    # Conexiones
    con1 = Conexion.obtener_conexion()
    print(con1)
    con2 = Conexion.obtener_conexion()
    print(con2)
    con3 = Conexion.obtener_conexion()
    print(con3)
    con4 = Conexion.obtener_conexion()
    print(con4)
    con5 = Conexion.obtener_conexion()
    print(con5)
    #conexión 6 => Error
    con6 = Conexion.obtener_conexion()
    print(con6)

    # Liberar la conexión #4
    Conexion.liberar_conexion(con4)
    print(con4)

    #Pedir de nuevo la conexión 6
    con6 = Conexion.obtener_conexion()
    print(con6)







