import RPi.GPIO as GPIO
import time, asyncio

class MotionSensor(object):    
    def __init__(self, pin):
        self.pin = pin
        self.setupGPIO()
        self.movementThreshold = 1
        self.readingDelay = 50

    def setupGPIO(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)

    def detectMotion(self):
        #count = 0
        #movementCount = 0
        movementDetected = False
        print("Starting sweep...")
        # while count < self.readingDelay:
        #     count += 1
        #     if GPIO.input(self.pin) == 1:
        #         movementCount += 1
        #         if movementCount > self.movementThreshold:
        #             movementDetected = True
        #             print("Movement Detected...")
        #             break         
        #     time.sleep(0.01)
        if GPIO.input(self.pin) == 1:
            movementDetected = True
        return movementDetected

    def activateLed(self):
        print("in alarm")
        if(self.ledPin > 0):
            print("alarm is on")
            GPIO.output(self.ledPin, GPIO.HIGH)
            asyncio.sleep(0.2)
            GPIO.output(self.ledPin, GPIO.LOW)
            asyncio.sleep(0.2)
    
    def deactivateLed(self):
        if(self.ledPin > 0):
            GPIO.output(self.ledPin, GPIO.LOW)

    def __getPin(self):
        return self.__pin
    
    def __setPin(self, value):
        self.__pin = value
    
    def __getLedPin(self):
        return self.__ledPin
    
    def __setLedPin(self, value):
        self.__ledPin = value
        GPIO.setup(value, GPIO.OUT)
    
    def __getMovementThreshold(self):
        return self.__movementThreshold
    
    def __setMovementThreshold(self, value):
        self.__movementThreshold = value

    def __getReadingDelay(self):
        return self.__readingDelay
    
    def __setReadingDelay(self, value):
        self.__readingDelay = value

    pin = property(__getPin, __setPin)

    ledPin = property(__getLedPin, __setLedPin)

    movementThreshold = property(__getMovementThreshold, __setMovementThreshold)

    readingDelay = property(__getReadingDelay, __setReadingDelay)

if __name__ == "__main__":
    m = MotionSensor(17)
    m.ledPin = 27
    while True:
        m.detectMotion()