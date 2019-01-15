class LedStripSettings(object):
    def __init__(self, *args, **kwargs):
        self.__id = 0
        self.__name = "LedStrip"
        self.__redPin = -1
        self.__greenPin = -1
        self.__bluePin  = -1
        self.__currentColor = None
        self.__currentIntensity = 100
    
    def __getredPin(self):
        return self.__redPin
    
    def __setredPin(self, value):
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

    def __getgreenPin(self):
        return self.__greenPin
    
    def __setgreenPin(self, value):
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
    
    def __getbluePin(self):
        return self.__bluePin
    
    def __setbluePin(self, value):
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
        self.__bluePin = value

    def __getcurrentIntensity(self):
        return self.__currentIntensity
    
    def __setcurrentIntensity(self, value):
        if not type(value) == int:
            try:
                value = int(value)
            except:
                value = -1
                pass
        if value > 100:
            value = 100
        if value < 0:
            value = 0
        self.__currentIntensity = value
    
    def __getcurrentColor(self):
        return self.__currentColor
    
    def __setcurrentColor(self, value):
        self.__currentColor = value
    
    def __getid(self):
        return self.__id
    
    def __setid(self, value):
        self.__id = value

    def __getname(self):
        return self.__name
    
    def __setname(self, value):
        self.__name = value

    name = property(__getname, __setname)

    id = property(__getid, __setid)

    redPin = property(__getredPin, __setredPin)

    greenPin = property(__getgreenPin, __setgreenPin)

    bluePin = property(__getbluePin, __setbluePin)

    currentIntensity = property(__getcurrentIntensity, __setcurrentIntensity)

    currentColor = property(__getcurrentColor, __setcurrentColor)
    