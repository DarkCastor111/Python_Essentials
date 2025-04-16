import mysql.connector

personas_db = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    port=3306,
    user="root",
    password="admin",
    database="personas_db"
)

# Sentencia Select :
#
# Crear un cursor
cur = personas_db.cursor()
# Ejecutar la sentencia SQL
cur.execute("SELECT * FROM personas")
# Obtener todos los resultados
resultados = cur.fetchall()
# Mostrar los resultados
for persona in resultados:
    print(f'### {persona}')
print()
# Cerrar el cursor y la conexión
cur.close()
personas_db.close()