import mysql.connector

def connect_to_mariadb():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="user",
        password="temperatur123",
        database="temperature_db"
    )
    print("Verbindung zur Datenbank aufgebaut...")
    return db_connection

def save_to_mariadb(temperature):
    db_connection = connect_to_mariadb()
    cursor = db_connection.cursor()

    query = "INSERT INTO temperatur (wert) VALUES (%s)"
    cursor.execute(query, (temperature,))

    db_connection.commit()
    cursor.close()
    db_connection.close()