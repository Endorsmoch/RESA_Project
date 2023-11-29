import mysql.connector

# Conectarse a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="123456789",
  database="ccna_2023"
)
def create_device_record():
    # Verificar si la conexión se realizó correctamente
    if mydb.is_connected():
        print('Conexión exitosa')

    # Realizar operaciones en la base de datos
    # Por ejemplo, crear un cursor y ejecutar una consulta
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ccna_2023.devices")

    # Obtener los resultados si es una consulta de selección
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    # Cerrar la conexión cuando hayas terminado
    mydb.close()