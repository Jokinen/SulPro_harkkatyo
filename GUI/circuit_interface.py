#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
from Circuit.TEMP_manager import TEMP_manager
try:
    import RPi.GPIO as GPIO
except ImportError:
    print("No RPi package, using DEV mode for circuit interface")
    CI_DEV = True

# Tässä on esimerkin vuoksi jotain koodia. Älä anna ohjata harhaan.
class circuit_interface:
    def __init__(self):
        self.TEMP = TEMP_manager()

    def setup(self):
        pass

    def get_temperature(self):
        return self.TEMP.get_temp_as_celsius()
