import RPi.GPIO as GPIO
import time
import json
import io
import os

class LedStripSetup:

    def __init__(self, *args, **kwargs):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.__redPin = -1
        self.loadSettings()
        print("Value of redPin: " + str(self.redPin))
        GPIO.setup(17, GPIO.OUT)

    def loadSettings(self):
        exist = os.path.isfile("settings.json")
        if exist:
            with open("settings.json") as f:
                data = json.load(f)
                self.redPin = data["redPin"]

    def get_redPin(self):
        return self.__redPin
    
    def set_redPin(self, value):
        self.__redPin = value

    redPin = property(get_redPin,set_redPin)

test = LedStripSetup()