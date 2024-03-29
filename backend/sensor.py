
import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 26
HARDWARE_HUM_PIN = 20
 

def readTemp(DHT_SENSOR = Adafruit_DHT.DHT11,DHT_PIN = 26):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        return temperature
    elif temperature == None:
        #print("Error reading sensor")
        return None
    
def readHum(DHT_SENSOR = Adafruit_DHT.DHT11,DHT_PIN = 26):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        #placeholder
        #humidity = 95
        return humidity
    elif humidity == None:
        #print("Error reading sensor")
        return None

def readHardwareHum(DHT_SENSOR=DHT_SENSOR, HARDWARE_HUM_PIN=HARDWARE_HUM_PIN):
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, HARDWARE_HUM_PIN)
    #placeholder
    #humidity = 50
    if humidity is not None and temperature is not None:
        return humidity
    elif humidity == None:
        #print("Error reading hardware sensor")
        return None
