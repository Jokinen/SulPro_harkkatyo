import RPi.GPIO as GPIO
import time

class PIR_manager:
    def __init__(self):
        self.SPI_CLK = 23
        self.SPI_CS = 24
        self.SPI_DATA = 16
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.SPI_CLK, GPIO.OUT)
        GPIO.setup(self.SPI_CS, GPIO.OUT)
        GPIO.setup(self.SPI_DATA, GPIO.IN, pull_up_down=GPIO.PUD_OFF)

    def read_status(self):
        clk = self.SPI_CLK
        cs = self.SPI_CS
        data = self.SPI_DATA

    	GPIO.output(clk, GPIO.LOW)
    	res = 0

    	for n in range(10):
    		time.sleep(0.05)
    		GPIO.output(cs, GPIO.HIGH)
    		MSB = 128
    		GPIO.output(cs, GPIO.LOW)
    		time.sleep(0.0005)
    		value = 0

    		for z in range(8):
    			if (GPIO.input(data)):
    				value = value + MSB
    			GPIO.output(clk, GPIO.HIGH)
    			time.sleep(0.0005)
    			GPIO.output(clk, GPIO.LOW)
    			MSB = MSB >> 1
    			time.sleep(0.0005)
    			result = value
    		GPIO.output(cs, GPIO.HIGH)
    		res = res + value

    	res = res / 10
    	return res
