import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def connect_to_mariadb():
    db_connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
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

def read_mariadb():
    db_connection = connect_to_mariadb()
    cursor = db_connection.cursor()

    cursor.execute("SELECT timestamp, wert FROM temperatur ORDER BY timestamp DESC LIMIT 10")
    temperatures = cursor.fetchall()

    cursor.close
    db_connection.close()
    return temperatures