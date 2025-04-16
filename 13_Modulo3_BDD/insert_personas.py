import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    port=3306,
    user="root",
    password="admin",
    database="personas_db"
)

# Sentencia Insert :
#
# Crear un cursor
cur = personas_db.cursor()
# Sentencia & Datos a insertar
sentencia = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
datos = [("Juan", "Pérez", 30), ("Ana", "Gómez", 25), ("Luis", "Martínez", 35)]
# Ejecutar la sentencia SQL
for dato in datos:
    cur.execute(sentencia, dato)
    # Mostrar el número de filas afectadas
    print(f'\n### Se ha insertado : {dato} - {cur.rowcount} registro insertado')

# Confirmar los cambios en la base de datos
personas_db.commit()

# Cerrar el cursor y la conexión
cur.close()
personas_db.close()