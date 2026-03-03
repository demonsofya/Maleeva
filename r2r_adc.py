import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01):
        self.dynamic_range = dynamic_range
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def dec_to_bin(self, val):
        return [int(el) for el in bin(val)[2:].zfill(8)]

    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio ,self.dec_to_bin(number))

    def sequential_counting_adc(self):
        num = 0
        self.number_to_dac(0)
        while True:
            cmp = GPIO.input(self.comp_gpio)
            if cmp > 0:
                return num

            num += 1
            if (num >= 256):
                num = 255

            self.number_to_dac(num)
            time.sleep(self.compare_time)
        return 255

    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        voltage = (code / 255.0) * self.dynamic_range

        return voltage

    def saccessive_approximation_adc(self):
        num = 0
        for bit in range(7, -1, -1):
            cmp = GPIO.input(self.comp_gpio)
            if cmp > 0:
                num -= 1 << bit
            else:
                num += 1 << bit
            
            if num >= 256:
                num = 255

            if num < 0:
                num = 0

            self.number_to_dac(num)
            time.sleep(self.compare_time)

        return num

    def get_sar_voltage(self):
        code = self.saccessive_approximation_adc()
        voltage = (code / 255.0) * self.dynamic_range

        return voltage


if __name__ == "__main__":
    DAC_RANGE = 3.30  # В

    adc = None
    try:
        adc = R2R_ADC(3.3, 0.01)
        
        while True:
            u = adc.get_sc_voltage()
            #u = adc.get_sar_voltage()
            print(f"U = {u:.3f} В")
            
            time.sleep(0.5)

    finally:
        GPIO.cleanup()