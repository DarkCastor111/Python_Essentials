import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    port=3306,
    user="root",
    password="admin",
    database="personas_db"
)

# Sentencia Update :
#
# Crear un cursor
cur = personas_db.cursor()
# Sentencia & Datos a insertar
sentencia = "UPDATE personas SET nombre = %s, apellido = %s, edad = %s WHERE id = %s"
datos = [("Pepe", "Choringo", 31, 4), ("Maria", "Lorca", 26, 5)]
# Ejecutar la sentencia SQL
for dato in datos:
    cur.execute(sentencia, dato)
    # Mostrar el número de filas afectadas
    print(f'\n### {dato} : Se ha actualizado {cur.rowcount} registro(s)')

# Confirmar los cambios en la base de datos
personas_db.commit()

# Cerrar el cursor y la conexión
cur.close()
personas_db.close()