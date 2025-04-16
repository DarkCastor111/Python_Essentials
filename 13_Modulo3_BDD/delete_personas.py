import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    port=3306,
    user="root",
    password="admin",
    database="personas_db"
)

# Sentencia Delete :
#
# Crear un cursor
cur = personas_db.cursor()
# Sentencia & Datos a insertar
sentencia = "DELETE FROM personas WHERE id = %s"
datos = [(3,), (6,)]
# Ejecutar la sentencia SQL
for dato in datos:
    cur.execute(sentencia, dato)
    # Mostrar el número de filas afectadas
    print(f'\n### id {dato} : Se ha eliminao {cur.rowcount} registro(s)')

# Confirmar los cambios en la base de datos
personas_db.commit()

# Cerrar el cursor y la conexión
cur.close()
personas_db.close()