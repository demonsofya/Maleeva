import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

button = 13
GPIO.setup(button, GPIO.IN)

phototrans = 6
GPIO.setup(phototrans, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(phototrans))
    time.sleep(0.05)