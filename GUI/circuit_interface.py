#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("No RPi package, using DEV mode for circuit interface")
    CI_DEV = True

# Tässä on esimerkin vuoksi jotain koodia. Älä anna ohjata harhaan.
class circuit_interface:
    def __init__(self):
        self.pin_temp_pin = 0 # ??
        self.temperature = 0
        self.setup()

    def setup(self):
        pass

    def get_temperature(self):
        return GPIO.input(self.pin_temp_pin)
