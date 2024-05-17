import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="basu8auzorc59y9pilys-mysql.services.clever-cloud.com",
        user="upjjlfvlgzsbwixm",
        password="tZSdTQUnSWzhB7kRw1B4",
        database="basu8auzorc59y9pilys"
    )

def main():
    try:
        # Conectarse a la base de datos
        db_connection = connect_to_database()
        
        if db_connection.is_connected():
            print("Conexión exitosa a la base de datos en Clever Cloud")
            
            # Realizar las operaciones que necesites aquí
            
    except mysql.connector.Error as err:
        print("Error al conectarse a la base de datos: {}".format(err))

if __name__ == "__main__":
    main()
