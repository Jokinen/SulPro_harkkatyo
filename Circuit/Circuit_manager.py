#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import RPi.GPIO as GPIO
from gui import info_display

class Circuit_manager:
    def __init__(self):
        self.motion_sensor_pin = 16
        self.pir_state = 0

        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(motion_sensor_pin, GPIO.IN)

    def loop(self):
        val = GPIO.input(self.motion_sensor_pin)
        if val == 1 and self.pir_state == 0:
            print "Motion detected"
            pir_state = 1
            self.start_GUI()
        elif val== 0 and self.pir_state == 1:
            print "Motion ended"
            pir_state = 0
            self.stop_GUI()

    def start_GUI(self):
        self.app = info_display(None)
        self.app.title('SulPro harkkatyö')
        self.app.mainloop()

    def stop_GUI(self):
        self.app.quit()
