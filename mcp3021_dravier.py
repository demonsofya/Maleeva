import time
import smbus

class MCP3021:
    def __init__(self, dynamic_range):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        
    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF

        number = (upper_data_byte << 6) | (lower_data_byte >> 2)

        return number

    def get_voltage(self):
        code = self.get_number()
        voltage = code * self.dynamic_range / 1023.0

        return voltage

if __name__ == "__main__":
    try:
        adc = MCP3021(5.2)
        
        while True:
            #voltage = adc.get_voltage()
            print(adc.get_voltage())
            time.sleep(1.0)

    finally:
        adc.deinit()