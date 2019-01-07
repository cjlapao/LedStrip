import RPi.GPIO as GPIO
import time

class MotionSensor(object):    
    def __init__(self, pin):
        self.pin = pin
        print("pin "+ str(self.pin))
        self.movementThreshold = 5
        self.readingDelay = 500
        self.setupGPIO()

    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)

    def detectMovement(self):
        count = 0
        movementCount = 0
        movementDetected = False
        while count < self.readingDelay:
            count += 1
            print("count "+ str(count))
            if GPIO.input(self.pin) == 1:
                movementCount += 1
                if movementCount > self.movementThreshold:
                    movementDetected = True
                    print("Movement Detected")
                    break
            time.sleep(0.05)
        return movementDetected

    def __getPin(self):
        return self.__pin
    
    def __setPin(self, value):
        self.__pin = value
    
    def __getMovementThreshold(self):
        return self.__movementThreshold
    
    def __setMovementThreshold(self, value):
        self.__movementThreshold = value

    def __getReadingDelay(self):
        return self.__readingDelay
    
    def __setReadingDelay(self, value):
        self.__readingDelay = value

    pin = property(__getPin, __setPin)

    movementThreshold = property(__getMovementThreshold, __setMovementThreshold)

    readingDelay = property(__getReadingDelay, __setReadingDelay)