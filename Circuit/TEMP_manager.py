import RPi.GPIO as GPIO
import time
import smbus

class TEMP_manager:
    def __init__(self):
        self.setup()

    def setup(self):
        self.bus = smbus.SMBus(0)    # I2C bus, using B rev1 so parameter is 0

        # TCN75A address, 0x48(72) (found with i2cdetect -y 0)
        # Select configuration register, 0x01(01)
        #		0x60(96)	12-bit ADC resolution
        self.bus.write_byte_data(0x48, 0x01, 0x60)

        time.sleep(0.5)

    def read(self):
        # TCN75A address, 0x48(72)
        # Read data back from 0x00(00), 2 bytes
        # temp MSB, temp LSB
        self.data = self.bus.read_i2c_block_data(0x48, 0x00, 2)

        return data

    def convert_data(self):
        data = self.read()

        # Convert the data to 12-bits
        temp = ((data[0] * 256) + (data[1] & 0xF0)) / 16
        if temp > 2047 :
          temp -= 4096

        return temp

    def get_temp_as_celsius(self):
        temp = self.convert_data()

        return temp * 0.0625
