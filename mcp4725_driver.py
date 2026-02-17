import smbus

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

    def set_voltage(self, voltage):
        self.pwm.start(voltage / self.dynamic_range * 100)
        #self.pwm.ChangeDutyCycle(voltage / self.dynamic_range * 255)