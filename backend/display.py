#controls actuators like lights and the display
import time
import RPi.GPIO as GPIO
import atexit
GPIO.setmode(GPIO.BCM)

HIGH_HUM_PIN = 17 
LOW_HUM_PIN = 18  
HIGH_TEMP_PIN = 19  
LOW_TEMP_PIN = 20   


GPIO.setup(HIGH_HUM_PIN, GPIO.OUT)
GPIO.setup(LOW_HUM_PIN, GPIO.OUT)
GPIO.setup(HIGH_TEMP_PIN, GPIO.OUT)
GPIO.setup(LOW_TEMP_PIN, GPIO.OUT)


#normal lights controlled by profile thresholds
def HighHumLight(on):
    # Control the High Humidity Warning Light
    if on:
        GPIO.output(HIGH_HUM_PIN, GPIO.HIGH)  
    else:
        GPIO.output(HIGH_HUM_PIN, GPIO.LOW)  

def LowHumLight(on):
    # Control the Low Humidity Warning Light
    if on:
        GPIO.output(LOW_HUM_PIN, GPIO.HIGH) 
    else:
        GPIO.output(LOW_HUM_PIN, GPIO.LOW)  

def HighTempLight(on):
    # Control the High Temperature Warning Light
    if on:
        GPIO.output(HIGH_TEMP_PIN, GPIO.HIGH)  
    else:
        GPIO.output(HIGH_TEMP_PIN, GPIO.LOW)  

def LowTempLight(on):
    # Control the Low Temperature Warning Light
    if on:
        GPIO.output(LOW_TEMP_PIN, GPIO.HIGH) 
    else:
        GPIO.output(LOW_TEMP_PIN, GPIO.LOW)  




# Define GPIO pins for seven-segment display (example pins, replace with actual connections)
SEGMENT_A = 14
SEGMENT_B = 15
SEGMENT_C = 1
SEGMENT_D = 23
SEGMENT_E = 25
SEGMENT_F = 8
SEGMENT_G = 7

# Define common pins for seven-segment display (example pins, replace with actual connections)
COMMON_1 = 17
COMMON_2 = 27

# map for displaying digits on the seven-segment display
DIGIT_MAP = {
    0: (SEGMENT_A, SEGMENT_B, SEGMENT_C, SEGMENT_D, SEGMENT_E, SEGMENT_F),
    1: (SEGMENT_B, SEGMENT_C),
    2: (SEGMENT_A, SEGMENT_B, SEGMENT_D, SEGMENT_E, SEGMENT_G),
    3: (SEGMENT_A, SEGMENT_B, SEGMENT_C, SEGMENT_D, SEGMENT_G),
    4: (SEGMENT_B, SEGMENT_C, SEGMENT_F, SEGMENT_G),
    5: (SEGMENT_A, SEGMENT_C, SEGMENT_D, SEGMENT_F, SEGMENT_G),
    6: (SEGMENT_A, SEGMENT_C, SEGMENT_D, SEGMENT_E, SEGMENT_F, SEGMENT_G),
    7: (SEGMENT_A, SEGMENT_B, SEGMENT_C),
    8: (SEGMENT_A, SEGMENT_B, SEGMENT_C, SEGMENT_D, SEGMENT_E, SEGMENT_F, SEGMENT_G),
    9: (SEGMENT_A, SEGMENT_B, SEGMENT_C, SEGMENT_D, SEGMENT_F, SEGMENT_G),
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(SEGMENT_A, GPIO.OUT)
GPIO.setup(SEGMENT_B, GPIO.OUT)
GPIO.setup(SEGMENT_C, GPIO.OUT)
GPIO.setup(SEGMENT_D, GPIO.OUT)
GPIO.setup(SEGMENT_E, GPIO.OUT)
GPIO.setup(SEGMENT_F, GPIO.OUT)
GPIO.setup(SEGMENT_G, GPIO.OUT)
GPIO.setup(COMMON_1, GPIO.OUT)
GPIO.setup(COMMON_2, GPIO.OUT)

def displayDigit(digit):
    # Display a digit on the seven-segment display
    segments = DIGIT_MAP.get(digit, ())
    for segment_pin in (SEGMENT_A, SEGMENT_B, SEGMENT_C, SEGMENT_D, SEGMENT_E, SEGMENT_F, SEGMENT_G):
        GPIO.output(segment_pin, GPIO.LOW if segment_pin not in segments else GPIO.HIGH)

def displayProfile(profile_id):
    # Display the profile ID on the seven-segment display
    if 0 <= profile_id <= 99:
        tens_digit = profile_id // 10
        ones_digit = profile_id % 10


        GPIO.output(COMMON_1, GPIO.LOW)
        GPIO.output(COMMON_2, GPIO.LOW)


        GPIO.output(COMMON_1, GPIO.HIGH)
        displayDigit(tens_digit)
        time.sleep(0.005)


        for segment_pin in (SEGMENT_A, SEGMENT_B, SEGMENT_C, SEGMENT_D, SEGMENT_E, SEGMENT_F, SEGMENT_G):
            GPIO.output(segment_pin, GPIO.LOW)

        # display ones digit on COMMON_2
        GPIO.output(COMMON_2, GPIO.HIGH)
        displayDigit(ones_digit)
        time.sleep(0.005)

atexit.register(GPIO.cleanup)
