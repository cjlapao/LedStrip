import os
import io
import json
from Color import Color

class Colors(object):
    def __init__(self, *args, **kwargs):
        self.__colors = []
        self.loadSettings()
    
    def loadSettings(self):
        exist = os.path.isfile("colors.json")
        if exist:
            with open("colors.json") as c:
                colors = json.load(c)
                colorsLen = len(colors)
                if colorsLen > 0:
                    for co in colors:
                        color = Color()
                        color.name = co["name"]
                        color.fromHex(co["value"])
                        self.__colors.append(color)
        print("Colors loaded from file")
    
    def __get_colors(self):
        return self.__colors
    
    def __set_colors(self, value):
        self.__colors = value

    items = property(__get_colors, __set_colors)