class LedStripSettings(object):
    def __init__(self, *args, **kwargs):
        self.__redPin = -1
        self.__greenPin = -1
        self.__bluePin  = -1
        self.__currentColor = None
        self.__currentIntensity = 100
    
    def __getRedPin(self):
        return self.__redPin
    
    def __setRedPin(self, value):
        if not type(value) == int:
            try:
                value = int(value)
            except:
                value = -1
                pass
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self.__redPin = value

    def __getGreenPin(self):
        return self.__greenPin
    
    def __setGreenPin(self, value):
        if not type(value) == int:
            try:
                value = int(value)
            except:
                value = -1
                pass
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self.__greenPin = value