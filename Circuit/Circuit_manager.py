#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from PIR_manager import PIR_manager
try:
    import RPi.GPIO as GPIO
    DEV = False
except ImportError:
    print("No RPi package, using DEV mode")
    DEV = True

from GUI import info_display

class Circuit_manager:
    def __init__(self):
        global DEV
        self.dev_mode = DEV

        self.PIR = PIR_manager()
        self.pir_state = 0
        self.movement_ongoing = False

        self.GUI_running = False
        self.start_GUI()

        if not self.dev_mode:
            self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD)

    def loop(self):
        if self.GUI_running is True:
            self.app.update_idletasks()
            self.app.update()

        if self.dev_mode:
            return

        val = self.PIR.read_status() # 0-255
        print val # for demonstration

        movement_begun = val >= 230 and not self.movement_ongoing
        movement_ended = val < 100 and self.movement_ongoing

        if movement_begun:
            self.movemet_ongoing = True
        if movement_ended:
            self.movement_ongoing = False

        if movement_begun and self.pir_state == 0:
            print "Motion detected, interface active, hiding GUI " + str(val)
            self.pir_state = 1
            self.hide_GUI()
        elif movement_begun and self.pir_state == 1:
            print "Motion detected, interface not active, showing GUI " + str(val)
            self.pir_state = 0
            self.show_GUI()

    def start_GUI(self):
        self.app = info_display.info_display(None)
        self.app.title('SulPro harkkatyö')
        self.hide_GUI()
        self.GUI_running = True

    def show_GUI(self):
        self.app.show()

    def hide_GUI(self):
        self.app.hide()

    def stop_GUI(self):
        self.app.close()
        self.GUI_running = False
