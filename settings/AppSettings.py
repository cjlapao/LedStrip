class AppSettings(object):
    def __init__(self, *args, **kwargs):
        self.__lightTimeout = 10000
        self.__defaultMhz = 50
        self.__dimmingDuration = 3
    
    def __getlightTimeout(self):
        return self.__lightTimeout
    
    def __setLightTimeout(self, value):
        self.__lightTimeout = value
    
    def __getdefaultMhz(self):
        return self.__defaultMhz
    
    def __setdefaultMhz(self, value):
        self.__defaultMhz = value