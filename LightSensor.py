class LightSensor(object):
    
    def __init__(self, *args, **kwargs):
        self.__pin = -1
    
    def __get_pin(self):
        return self.__pin
    
    def __set_pin(self, value):
        self.__pin = value
    
    pin = property(__get_pin, __set_pin)