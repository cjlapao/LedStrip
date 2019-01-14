from settings.LedStripSettings import LedStripSettings
from LightSensor import LightSenso

class MotionSensorSettings(object):
    def __init__(self, *args, **kwargs):
        self.__pin = -1
        self.__ledStrips = [LedStrip()]
        self.__lightSensors = [LightSensor]

    def __getPin(self):
        return self.__pin
    
    def __setPin(self, value):
        self.__pin = value

    def __getLedStrips(self):
        return self.__ledStrips

    def __getLightSensors(self):
        return self.__lightSensors

    pin = property(__getPin, __setPin)

    ledStrips = property(__getLedStrips)

    __lightSensors
        
    