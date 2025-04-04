import time
import threading
from sensor import read_temp
from database import save_to_mariadb
from webserver import start_webserver


def read_and_save_temperature():
    while True:
        temperature = read_temp()
        print(f"Aktuelle Temperatur: {temperature}°C")
        save_to_mariadb(temperature)
        time.sleep(60)

def start_application():
    temperature_thread = threading.Thread(target=read_and_save_temperature)
    temperature_thread.daemon = True
    temperature_thread.start()

    start_webserver()

if __name__ == "__main__":
    start_application()