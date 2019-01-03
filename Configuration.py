import json
import io
import os
from LedStrip import LedStrip
from LightSensor import LightSensor
from Colors import Colors

class Configuration:

    def __init__(self, *args, **kwargs):
        self.__items = object
        self.__ledStrips = []
        self.__lightSensor = LightSensor()
        self.__colors = Colors()
        self.loadSettings()
        print("Value of redPin: " + self.items["ledStrips"][0]["name"])

    def loadSettings(self):
        exist = os.path.isfile("settings.json")
        if exist:
            with open("settings.json") as f:
                self.__items = json.load(f)
                if "ledStrips" in self.__items:
                    ledStripsLen = len(self.__items["ledStrips"])
                    if (ledStripsLen > 0):
                        for ledStrip in self.__items["ledStrips"]:
                            obj = LedStrip()
                            obj.name = ledStrip["name"]
                            obj.redPin = ledStrip["redPin"]
                            obj.greenPin = ledStrip["greenPin"]
                            obj.bluePin = ledStrip["bluePin"]
                            self.__ledStrips.append(obj)
                if "lightSensor" in self.__items:
                    self.__lightSensor.pin = self.__items["lightSensor"]
    
    def _get_items(self):
        return self.__items
    
    def _set_items(self, value):
        self.__items = value 
    
    def _get_lightSensor(self):
        return self.__lightSensor
    
    def _set_lightSensor(self, value):
        self.__lightSensor = value
    
    def _get_LedStrips(self):
        return self.__ledStrips
    
    def _set_ledStrips(self, value):
        self.__ledStrips = value

    def __get_colors(self):
        return self.__colors
    
    def __set_colors(self, value):
        self.__colors = value

    def printLedStrips(self):
        for ledStrip in self.__ledStrips:
            print("name: " + ledStrip.name)
    
    items = property(_get_items, _set_items)

    ledStrips = property(_get_LedStrips, _set_ledStrips)

    lightSensor = property(_get_lightSensor, _set_lightSensor)

    colors = property(__get_colors, __set_colors)