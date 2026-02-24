import sugnal_generator as sg
import time 

import RPi.GPIO as GPIO

amplitude = 1
signal_frequency = 10
sampling_frequency = 1000

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frquency, dynamic_range, verbose = False):
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(gpio_pin, GPIO.OUT)
            
            self.gpio_pin = gpio_pin
            self.dynamic_range = dynamic_range
            self.verbose = verbose

            self.pwm = GPIO.PWM(gpio_pin, pwm_frquency)

    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        self.pwm.start(voltage / self.dynamic_range * 100)
        #self.pwm.ChangeDutyCycle(voltage / self.dynamic_range * 255)


try:
    dac = PWM_DAC(12, 500, 3.290, True)

    while True:
        voltage = sg.get_sin_wave_amplitude(signal_frequency, time.time()) * 3
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
    

finally:
    dac.deinit()