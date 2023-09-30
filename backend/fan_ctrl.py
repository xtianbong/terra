import RPi.GPIO as GPIO

# Set the GPIO pin number to control the fan
FAN_PIN = 16  # Replace with your actual GPIO pin number

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

def fanOn():
    # don't think pwm speed control is necessary here, we'll just run the fan at 100%
    GPIO.output(FAN_PIN, GPIO.HIGH)

def fanOff():
    GPIO.output(FAN_PIN, GPIO.LOW)
