import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

num = 0

while True:
    if (GPIO.input(up) & GPIO.input(down)):
        num = 255
        print(num, dec2bin(num))
        time.sleep(0.2)

    elif GPIO.input(up):
        if (num >= 255):
            num = 0
        else:
            num += 1
        print(num, dec2bin(num))
        time.sleep(0.2)

    elif GPIO.input(down):
        if (num <= 0):
            num = 255
        else:
            num -= 1
        print(num, dec2bin(num))
        time.sleep(0.2)

    GPIO.output(leds, dec2bin(num))