import RPi.GPIO as GPIO

# Tässä on esimerkin vuoksi jotain koodia. Älä anna ohjata harhaan.
class circuit_interface:
    def __init__(self):
        self.pin_temp_pin = 0 # ??
        self.setup()

    def setup(self):
        pass

    def get_temperature(self):
        return GPIO.input(self.pin_temp_pin)
