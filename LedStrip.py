import RPi.GPIO as GPIO
from Color import Color

class LedStrip:
    def __init__(self, red, green, blue):
        self.defMhz = 50
        self._redPin = red
        self._greenPin = green
        self._bluePin = -blue

        self._redPinValue = 0
        self._greenPinValue = 0
        self._bluePinValue = 0
        self._name = ""
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.setupGPIO()
    
    def setupGpi(self, pin, value):
        GPIO.setup(pin, GPIO.OUT)
        pin = value
        print("Pin Setup "+ pin)
    
    def setupGPIO(self):
        GPIO.setup(self.redPin, GPIO.OUT)
        GPIO.setup(self.greenPin, GPIO.OUT)
        GPIO.setup(self.bluePin, GPIO.OUT)
        self.pwmR = GPIO.PWM(self.redPin, self.defMhz)
        self.pwmG = GPIO.PWM(self.greenPin, self.defMhz)
        self.pwmB = GPIO.PWM(self.bluePin, self.defMhz)
        self.pwmR.start(0)
        self.pwmG.start(0)
        self.pwmB.start(0)
        print("GPIO setup finished")

    def setColor(self, name):
        color = Color()
        try:
            color.fromHex(name)
            self.redPinValue = color.red
            self.greenPinValue = color.green
            self.bluePinValue = color.blue
            self.pwmR.ChangeDutyCycle(color.red / 255 * 100)
            self.pwmG.ChangeDutyCycle(color.green / 255 * 100)
            self.pwmB.ChangeDutyCycle(color.blue / 255 * 100)
        except:
             pass

    def _get_name(self):
        return self._name

    def _set_name(self, value):
        self._name = value

    def get_redPin(self):
        return self._redPin
    
    def set_redPin(self, value):
        print("testing red")
        self.setupGpi(self._redPin, value)
        self._redPin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, 0)
    
    def _get_greenPin(self):
        return self._greenPin
    
    def _set_greenPin(self, value):
        self._greenPin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, 0)
    
    def _get_bluePin(self):
        return self._bluePin
    
    def _set_bluePin(self, value):
        self._bluePin = value
        GPIO.setup(value, GPIO.OUT)
        GPIO.output(value, 0)

    def _get_redPinValue(self):
        return self._redPinValue
    
    def _set_redPinValue(self, value):
        self._redPinValue = value
        GPIO.output(self._redPin, self._redPinValue)

    def _get_greenPinValue(self):
        return self._greenPinValue
    
    def _set_greenPinValue(self, value):
        self._greenPinValue = value
        GPIO.output(self._greenPin, self._greenPinValue)

    def _get_bluePinValue(self):
        return self._bluePinValue
    
    def _set_bluePinValue(self, value):
        self._bluePinValue = value
        GPIO.output(self._bluePin, self._bluePinValue)

    name = property(_get_name, _set_name)

    redPin = property(get_redPin, set_redPin)

    redPinValue = property(_get_redPinValue, _set_redPinValue)

    greenPin = property(_get_greenPin, _set_greenPin)

    greenPinValue = property(_get_greenPinValue, _set_greenPinValue)

    bluePin = property(_get_bluePin, _set_bluePin)

    bluePinValue = property(_get_bluePinValue, _set_bluePinValue)