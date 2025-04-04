# temperatur-projekt

# Temperaturüberwachungssystem mit Flask und MySQL

Ein einfaches Python-basiertes Projekt zur Überwachung der Temperatur eines Sensors und Speicherung der Daten in einer MySQL/MariaDB-Datenbank. Das Projekt verwendet Flask als Webframework, um die letzten Temperaturwerte anzuzeigen.

## Beschreibung

Dieses Projekt sammelt Temperaturdaten von einem 1-Wire-fähigen Sensor, speichert die Werte in einer MySQL/MariaDB-Datenbank und stellt sie auf einer Webseite zur Verfügung. Die letzten 10 Temperaturwerte können über den Webserver überwacht werden.

## Vorraussetzungen

- Python 3.11.2
- MariaDB
- Flask
- 1-Wire Temperatursensor (z.B. DS18B20)

## Installation

### Schritt 1: Repository klonen

```bash
git clone https://github.com/schmilipppp/temperatur-projekt.git
cd temperatur-projekt
```

### Schritt 2: MariaDB installieren und konfigurieren

1. MariaDB installieren
2. Datenbank nach folgendem Konzept erstellen:

```sql
CREATE DATABASE temperatur_db;
USE temperatur_db;

CREATE TABLE temperatur (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    wert DECIMAL(5,2) NOT NULL
);
```

### Schritt 3: Konfiguration der Datenbankverbindung

Für die Konfiguration der Verbindung zur MariaDB-Datenbank werden Umgebungsvariablenm in Form einer .env Datei verwendet. Durch diese Datei können sensible Daten sicher verwaltet werden.

```env
DB_HOST=localhost
DB_USER=user
DB_PASSWORD=temperatur123
DB_NAME=temperatur_db
```

Python greift auf die Datenbank in folgendem Syntax zu:

```python
def connect_to_mariadb():
    db_connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
```


### Schritt 4: Sensor konfigurieren

Nach erfolgreicher Verbindung wird der Sensor über den Pfad `/sys/bus/w1/devices/28-xxxxxxxxxxxx/temperature` angesprochen.

### Schritt 5: Anwendung starten

Das Projekt startet, indem  die `main.py` ausgeführt wird. Dies startet das Programm, welches die Temperaturdaten liest und in die Datenbank speichert.

```bash
python main.py
```

Die Webseite kann unter dem Port 5000 aufgerufen werden.

## Beispiel

Die Webseite zeigt die letzten 10 gespeicherten Temperaturwerte aus der Datenbank in einer Tabelle an.

| Timestamp            | Wert (°C)  |
|----------------------|------------|
| 2025-04-04 12:34:56  | 22.50      |
| 2025-04-04 12:33:56  | 22.48      |
| ...                  | ...        |

## Technologien und Tools

- **Python 3.11.2** für die Programmiersprache
- **Flask** für das Webframework
- **MariaDB** für die Datenbank
- **DS18B20** für die Temperaturmessung