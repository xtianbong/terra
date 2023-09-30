import csv
import subprocess
import os
import RPi.GPIO as GPIO
from sensor import *
import time
from display import *

# GPIO pin for the push button (BCM numbering)
BUTTON_PIN = 12

# Placeholder values
interval = 1
interval_seconds = interval * 3600
hum_threshold = [70, 90]
temp_threshold = [20, 30]
fanning_duration = 60

last_fan = 0
profile_id = 0

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def humCheck(hum):
    if hum >= hum_threshold[1]:
        return "high"
    if hum <= hum_threshold[0]:
        return "low"
    else:
        return "normal"

def create_default_csv():
    # Create a default CSV file with some default values
    with open('profiles.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'max_temp', 'min_temp', 'max_hum', 'min_hum', 'fan_int', 'fan_dur']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Add default profile data
        default_profile = {
            'id': 1,
            'max_temp': 30,
            'min_temp': 20,
            'max_hum': 90,
            'min_hum': 70,
            'fan_int': 1,
            'fan_dur': 60,
        }
        writer.writerow(default_profile)

def getProfile(i):
    profiles = []  # 2D list to store all profiles

    if not os.path.exists('profiles.csv'):
        # If 'profiles.csv' does not exist, create a default CSV file
        create_default_csv()

    with open('profiles.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # Skip the first row (column titles)
        next(reader)

        for row in reader:
            # Convert relevant columns to integers
            profile = [
                int(row['id']),
                int(row['max_temp']),
                int(row['min_temp']),
                int(row['max_hum']),
                int(row['min_hum']),
                int(row['fan_int']),
                int(row['fan_dur'])
            ]
            profiles.append(profile)

    # Check if i is not over the number of profiles (profiles start at 1)
    if i >= len(profiles):
        i = i - len(profiles)
    profile_data = profiles[i]

    # Populate the relevant variables based on the profile data
    global current_profile_id, hum_threshold, temp_threshold, interval, fanning_duration
    current_profile_id = i
    hum_threshold = [profile_data[3], profile_data[4]]
    temp_threshold = [profile_data[1], profile_data[2]]
    interval = profile_data[5]
    fanning_duration = profile_data[6]

# Main function
start_time = time.time()

# Initialize variables for button press handling
button_pressed = False
button_last_state = False

while True:
    hum = readHum()
    temp = readTemp()

    #only run code if the sensor is working maybe shutdown the pi if the hardware sensor is offline idk
    if hum != None and temp != None:
        #display current profile
        displayProfile(current_profile_id)

        # Toggle warning lights
        if hum >= hum_threshold[1]:
            print("HIGH HUMIDITY")
            HighHumLight(True)
        elif hum < hum_threshold[1]:
            HighHumLight(False)

        if hum <= hum_threshold[0]:
            print("LOW HUMIDITY")
            LowHumLight(True)
        elif hum > hum_threshold[0]:
            LowHumLight(False)

        if temp >= temp_threshold[1]:
            print("HIGH TEMP")
            HighTempLight(True)
        elif temp < temp_threshold[1]:
            HighTempLight(False)

        if temp <= temp_threshold[0]:
            LowTempLight(True)
            print("LOW TEMP")
        elif temp > temp_threshold[0]:
            LowTempLight(False)

        


        # Get the elapsed time in seconds
        elapsed_time = time.time() - start_time
        # If the specified time interval has passed and humidity is above the lower threshold, turn on the fan
        if elapsed_time % interval_seconds < 3 and hum > hum_threshold[0]:
            fanning_timer = fanning_duration

        
        # if on the hour, humidity is above the upper threshold, and the fan is not currently on, turn on the fan
        if elapsed_time % 3600 < 3 and hum >= hum_threshold[1] and fanning_timer <= 0:
            fanning_timer = fanning_duration

        # Update the time left with the fan on every cycle
        if fanning_timer >= 0:
            fanOn()
            fanning_timer -= 3
            print("Fan on. {} seconds left.".format(fanning_timer))
            # Record the time the fan turns off
            if fanning_timer <= 0:
                last_fan = time.time()
                print("Fan off")
        else:
            fanOff()

        # Check for a button press
        button_state = GPIO.input(BUTTON_PIN)

        if button_state != button_last_state:
            if button_state == GPIO.LOW:
                button_pressed = True
            else:
                button_pressed = False

        if button_pressed:
            fanOff()
            current_profile_id = current_profile_id + 1
            print("Switching to profile {}".format(current_profile_id))
            getProfile(current_profile_id + 1)

        button_last_state = button_state

        time.sleep(3)
        print("Temperature: {}°C, Humidity: {}%".format(readTemp(), readHum()))

        #save data to logs at the beginning and after every hour
        if elapsed_time % 3600 < 3 or elapsed_time > 10: #set time threshold to 10 incase there is a delay for some reason. wil mean 2-3 redundant logs but that is ok
            save_logs(hum, temp, hum_threshold, temp_threshold, last_fan, current_profile_id, hardware_hum)

        #hardware humidity monitor placed at the end to make sure all data is collected for logs
        hardwareHum = readHardwareHum()
        if hum >= 70:
            print("HIGH HUMIDITY IN HARDWARE SHUTTING DOWN")
            save_logs(hum, temp, hum_threshold, temp_threshold, last_fan, current_profile_id, hardware_hum)
            subprocess.run(["sudo", "poweroff"])
atexit.register(GPIO.cleanup)