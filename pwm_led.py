import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

pwm = GPIO.PWM(led, 200) # частота - 200 Гц, это объект управления сигналом
duty = 0.0 # коэффициент заполнения
pwm.start(duty)

while True:
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.02)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0