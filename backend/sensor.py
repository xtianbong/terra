import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 26
 

def readTemp(DHT_SENSOR = Adafruit_DHT.DHT11,DHT_PIN = 26):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature
    else:
        print("Error reading sensor")
        return None
    
def readHum(DHT_SENSOR = Adafruit_DHT.DHT11,DHT_PIN = 26):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return humidity
    else:
        print("Error reading sensor")
        return None