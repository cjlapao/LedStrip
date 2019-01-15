class Color(object):
    def __init__(self):
        self.red = 0
        self.green = 0
        self.blue = 0
        self.name = "none"

    def __RgbToHex(self, red = None, green = None, blue = None):
        red = int(round(red,0))
        if red > 255:
            red = 255
        if red < 0:
            red = 0
        green = int(round(green,0))
        if green > 255:
            green = 255
        if green < 0:
            green = 0
        blue = int(round(blue, 0))
        if blue > 255:
            blue = 255
        if blue < 0:
            blue = 0
        #print("red" + str(red) +", green" + str(green) +", blue" + str(blue))
        sRed = hex(red)[2:]
        sGreen = hex(green)[2:]
        sBlue = hex(blue)[2:]
        if len(sRed) == 1:
            sRed = "0" + sRed
        if len(sGreen) == 1:
            sGreen = "0" + sGreen
        if len(sBlue) == 1:
            sBlue = "0" + sBlue
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
        self.__red = int(round(value,0))
    
    def __get_green(self):
        return self.__green
    
    def __set_green(self, value):
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self.__green = int(round(value,0))
    
    def __get_blue(self):
        return self.__blue
    
    def __set_blue(self, value):
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        self.__blue = int(round(value,0))
    
    def __getweb(self):
        return self.toHex()

    def fromHex(self, value):
        if "#" in value:
            value = str(value).replace("#","")
        self.red = int(value[0:2], 16)
        self.green = int(value[2:-2], 16)
        self.blue = int(value[4:], 16)

    def toHex(self):
        return self.__RgbToHex(self.red, self.green, self.blue)    

    def lighten(self, percentage = 10):
        #print("previous color "+self.toHex())
        self.red = self.red - (self.red * (percentage / float(100)))
        self.green = self.green - (self.green * (percentage / float(100)))
        self.blue = self.blue - (self.blue * (percentage / float(100)))
        #print("percentage" + str(percentage) +" red" + str(self.red) +", green" + str(self.green) +", blue" + str(self.blue))
        #print("new lighter color "+self.toHex())
        return self.toHex()
        
    def darken(self, percentage = 10):
        #print("previous color "+self.toHex())
        self.red = self.red - (self.red * (percentage / float(100)))
        self.green = self.green - (self.green * (percentage / float(100)))
        self.blue = self.blue - (self.blue * (percentage / float(100)))
        #print("percentage" + str(percentage) +" red" + str(self.red) +", green" + str(self.green) +", blue" + str(self.blue))
        #print("new darker color "+self.toHex())
        return self.toHex()
    
    def getDarkerVersion(self, percentage = 10):
        #print("Getting  darken color version")
        red = 0
        green = 0
        blue = 0
        red = self.red - (self.red * (percentage / float(100)))
        green = self.green - (self.green * (percentage / float(100)))
        blue = self.blue - (self.blue * (percentage / float(100)))
        #print("percentage" + str(percentage) +" red" + str(red) +", green" + str(green) +", blue" + str(blue))
        #print("new darker color "+self.__RgbToHex(red,green,blue))
        return self.__RgbToHex(red, green, blue)

    def getLighterVersion(self, percentage = 10):
        #print("Getting  darken color version")
        red = 0
        green = 0
        blue = 0
        red = self.red + (self.red * (percentage / float(100)))
        green = self.green + (self.green * (percentage / float(100)))
        blue = self.blue + (self.blue * (percentage / float(100)))
        #print("percentage" + str(percentage) +" red" + str(red) +", green" + str(green) +", blue" + str(blue))
        #print("new darker color "+self.__RgbToHex(red,green,blue))
        return self.__RgbToHex(red, green, blue)

    name = property(__get_name,  __set_name)
    red = property(__get_red, __set_red)
    green = property(__get_green, __set_green)
    blue = property(__get_blue, __set_blue)
    web = property(__getweb)

if __name__ == "__main__":
    color = Color()
    color.fromHex("#ff0000")
    intensity = 0
    while intensity <100:
        intensity += 2
        color.getDarkerVersion(intensity)
