import sugnal_generator as sg
import time
import numpy

import smbus

def get_tri_wave_amplitude(freq,t,amplitude):
    return (numpy.arcsin(numpy.sin(2*numpy.pi*freq*t)) * 2 * amplitude / numpy.pi) + amplitude


def wait_for_sampling_period(sampling_frequency):
    time.sleep(1/sampling_frequency)

amplitude = 2.5
signal_frequency = 10
sampling_frequency = 1000


class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАМ можно одавать только целые числа")

        if not (0 <= number <= 4095):
                print("Число выхожит за разрядность VCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print((f"Число: {number}, отправленные по I2C даные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n"))

    def set_voltage(self, voltage):
        self.set_number(int(voltage / 5.5 * 4095))
        #self.set_number(3606)

try:
    dac = MCP4725(5.5)

    while True:
        voltage = get_tri_wave_amplitude(signal_frequency, time.time(), amplitude)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()