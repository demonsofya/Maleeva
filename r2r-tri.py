import numpy
import time
import RPi.GPIO as GPIO


def get_tri_wave_amplitude(freq,t,amplitude):
    return (numpy.arcsin(numpy.sin(2*numpy.pi*freq*t)) * 2 * amplitude / numpy.pi) + amplitude


def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)


amplitude = 1
signal_frequency = 10
sampling_frequency = 1000

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
            self.gpio_bits = gpio_bits
            self.dynamic_range = dynamic_range
            self.verbose = verbose
            
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_number(self, number):
        GPIO.output(self.gpio_bits ,[int(element) for element in bin(number)[2:].zfill(8)])

    def set_voltage(self, voltage):
        self.set_number(int(voltage / self.dynamic_range * 255))


try:
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)

    while True:
            voltage = get_tri_wave_amplitude(signal_frequency, time.time(), amplitude)
            print(voltage)
            dac.set_voltage(voltage)
            wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()