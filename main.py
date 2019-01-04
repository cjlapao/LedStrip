import RPi.GPIO as GPIO
import time
from LedStrip import LedStrip
from LightSensor import LightSensor
from Configuration import Configuration
from Color import Color

conf = Configuration

def __init__():
    gpioStartUp()
    conf = Configuration()
    color = Color()
    color.fromHex("#fafbfc")
    print("red: " + str(color.red) + ", green: "+  str(color.green) + ", blue: "+ str(color.blue))
    test = color.toHex()
    print("Color Hex: "+ test)
    if len(conf.colors.items) > 0:
        for color in conf.colors.items:
            print("Color: " + color.name + ", value: " + color.toHex())
    
    colorVal = raw_input("Type in the color:")
    conf.ledStrips[0].setColor(colorVal)

    print("LedStrip on: RED "+str(conf.ledStrips[0].redPinValue) + ", Green " + str(conf.ledStrips[0].greenPinValue) + ", Blue " +str(conf.ledStrips[0].bluePinValue))

def gpioStartUp():
    #GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

__init__()

