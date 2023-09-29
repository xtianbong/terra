from sensor import *
import time

while True:
    time.sleep(3);
    print("Temperature: {}°C, Humidity: {}%".format(readTemp(), readHum()))
