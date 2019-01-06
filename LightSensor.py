import time
import RPi.GPIO as GPIO

class LightSensor(object):
    
    def __init__(self, sensorPin):
        try:
            self.__pin = int(sensorPin)
        except:
            self.__pin = 4
        self.setupGPIO()
    
    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def getLightIntensity(self):
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.setup(self.pin, GPIO.IN)
        count = 0        
        while (GPIO.input(self.pin) == GPIO.LOW):
            count += 1
        return count

    def isDay(self):
        intensity = self.getLightIntensity()
        if intensity >= 0 and intensity <= 600:
            return True
        else: 
            return False
    
    def isNight(self):
        intensity = self.getLightIntensity()
        if intensity >= 601 and intensity <= 2000:
            return True
        else: 
            return False

    def __get_pin(self):
        return self.__pin
    
    def __set_pin(self, value):
        self.__pin = value
    
    pin = property(__get_pin, __set_pin)