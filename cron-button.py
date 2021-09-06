import time
from datetime import datetime
import RPi.GPIO as GPIO

# the pin numbers refer to the board connector not the chip
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Door closed
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
# Door open
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
# Open/Close Button
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)

def pushButton():
    GPIO.output(7, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(7, GPIO.LOW)
    time.sleep(2)

# If the garage is open, close it.
def closeIfOpen():
    if GPIO.input(18) == GPIO.LOW:
        print("Garage is Open")
        pushButton()

closeIfOpen()
