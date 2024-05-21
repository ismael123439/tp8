import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="borgutwop9xvo57oqrfa-mysql.services.clever-cloud.com",
        user="umrk43qubdfxq6ga",
        password="nLxs4jFFmdwVIwWYDBgd",
        database="borgutwop9xvo57oqrfa"
    )

def insertar_usuario(cursor, nombre, email):
    sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
    valores = (nombre, email)
    cursor.execute(sql, valores)

def main():
    db_connection = None
    try:
        db_connection = connect_to_database()
        
        if db_connection.is_connected():
            print("Conexión exitosa a la base de datos en Clever Cloud")
            
    except mysql.connector.Error as err:
        print("Error al conectarse a la base de datos: {}".format(err))

if __name__ == "__main__":
    main()
