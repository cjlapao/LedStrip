class LightSensorSettings(object):
    def __init__(self, pin):
        self.pin = pin
        self.__dayNightThreshold = 600
    
    def __getPin(self):
        return self.__pin
    
    def __setPin(self, value):
        if(not type(value)  == int):
            value = -1
        self.__pin = value

    def __getDayNightThreshold(self):
        return self.__dayNightThreshold
    
    def __setDayNightThreshold(self, value):
        if(not type(value) == int):
            value = 600
        self.__dayNightThreshold = value
    
    pin = property(__getPin, __setPin)

    dayNightThreshold = property(__getDayNightThreshold, __setDayNightThreshold)