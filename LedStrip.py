import RPi.GPIO as GPIO
from Color import Color

class LedStrip:
    def __init__(self, *args, **kwargs):
        self.__redPin = -1
        self.__greenPin = -1
        self.__bluePin = -1

        self.__redPinValue = 0
        self.__greenPinValue = 0
        self.__bluePinValue = 0
        self.__name = ""
    
    def setColor(self, name):
        color = Color()
        try:
            color.fromHex(name)
            self.redPinValue = color.red
            self.greenPinValue = color.green
            self.bluePinValue = color.blue
        except:
             pass

    def _get_name(self):
        return self.__name

    def _set_name(self, value):
        self.__name = value

    def _get_redPin(self):
        return self.__redPin
    
    def _set_redPin(self, value):
        self.__redPin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, 0)
    
    def _get_greenPin(self):
        return self.__greenPin
    
    def _set_greenPin(self, value):
        self.__greenPin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, 0)
    
    def _get_bluePin(self):
        return self.__bluePin
    
    def _set_bluePin(self, value):
        self.__bluePin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, 0)

    def _get_redPinValue(self):
        return self.__redPinValue
    
    def _set_redPinValue(self, value):
        self.__redPinValue = value
        GPIO.output(self.__redPin, self.__redPinValue)

    def _get_greenPinValue(self):
        return self.__greenPinValue
    
    def _set_greenPinValue(self, value):
        self.__greenPinValue = value
        GPIO.output(self.__greenPin, self.__greenPinValue)

    def _get_bluePinValue(self):
        return self.__bluePinValue
    
    def _set_bluePinValue(self, value):
        self.__bluePinValue = value
        GPIO.output(self.__bluePin, self.__bluePinValue)

    name = property(_get_name, _set_name)

    redPin = property(_get_redPin, _set_redPin)

    redPinValue = property(_get_redPinValue, _set_redPinValue)

    greenPin = property(_get_greenPin, _set_greenPin)

    greenPinValue = property(_get_greenPinValue, _set_greenPinValue)

    bluePin = property(_get_bluePin, _set_bluePin)

    bluePinValue = property(_get_bluePinValue, _set_bluePinValue)