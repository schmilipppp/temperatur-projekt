import time

temperature_path = "/sys/bus/w1/devices/28-3c2ae3813dec/temperature"

def read_temp():
    with open(temperature_path, 'r') as f:
        temp_raw = f.read().strip()
        return float(temp_raw) / 1000.0