class Color(object):
    def __init__(self, *args, **kwargs):
        self.__red = 0
        self.__green = 0
        self.__blue = 0
        self.__name = ""

    def fromHex(self, value):
        if "#" in value:
            value = str(value).replace("#","")
        self.red = int(value[0:2], 16)
        self.green = int(value[2:-2], 16)
        self.blue = int(value[4:], 16)

    def toHex(self):
        sRed = hex(self.red)[2:]
        sGreen = hex(self.green)[2:]
        sBlue = hex(self.blue)[2:]
        return "#"+ sRed + sGreen + sBlue
    
    def __get_name(self):
        return self.__name
    
    def __set_name(self, value):
        self.__name = value

    def __get_red(self):
        return self.__red
    
    def __set_red(self, value):
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self.__red = value
    
    def __get_green(self):
        return self.__green
    
    def __set_green(self, value):
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self.__green = value
    
    def __get_blue(self):
        return self.__blue
    
    def __set_blue(self, value):
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self.__blue = value
    
    name = property(__get_name,  __set_name)
    red = property(__get_red, __set_red)
    green = property(__get_green, __set_green)
    blue = property(__get_blue, __set_blue)