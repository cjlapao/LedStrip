import RPi.GPIO as GPIO
import time, argparse
from LedStrip import LedStrip
from LightSensor import LightSensor
from Configuration import Configuration
from Color import Color

class LedStripController(object):
    def __init__(self, *args, **kwargs):
        self.strip = 0
        self.conf = Configuration()
        self.conf.lightSensor
        self.timeTo = 10000
        print("Configuration loaded")
        self.cmd = None
        self.color = None
        for arg in args:
            if arg.cmd:
                if arg.cmd == "motion":
                    self.startMotionSensor()
                elif arg.cmd == "light":
                    self.getLightSensorValue()
                elif arg.cmd == "color":
                    self.setColor()
                else:
                    self.mainMenu()
            else:
                self.mainMenu()

    def mainMenu(self):
        stripSelector = input("Select Strip[0]: ")
        if not stripSelector:
            stripSelector = "0"
        
        if stripSelector == "quit":
            self.close()
        else:
            try:
                if int(stripSelector) > -1 and int(stripSelector) < self.conf.ledStripsCount:
                    self.getLedStripCommand(stripSelector)
            except Exception as e:
                print(e)
                print("Invalid strip number")
                self.mainMenu()

    def getLedStripCommand(self, ledStrip):
        strip = int(ledStrip)
        command = input("[LedStrip"+ str(strip) +"] Select Command: ")
        if command.lower() == "color":
            self.setColor()
        elif command.lower() == "fadein":
            self.setFadeIn()
        elif command.lower() == "fadeout":
            self.setFadeOut()
        elif command.lower() == "intensity":
            self.setIntensity()
        elif command.lower() == "lightsensor":
            self.getLightSensorValue()
        elif command.lower() == "motionsensor":
            self.startMotionSensor()
        elif command.lower() == "quit":
            self.close()
        elif command.lower() == "back":
            self.mainMenu()
        else:
            self.help()
            self.getLedStripCommand(strip)

    def setColor(self):
        colorVal = ""
        while True:
            colorVal = input("[LedStrip"+ str(self.strip) +"] What color would you like: ")
            if colorVal == "quit":
                break
            elif colorVal == "back":
                break
            if "#" in colorVal:
                self.conf.ledStrips[self.strip].setColor(colorVal)
            else:
                color = self.conf.getColor(colorVal)
                if not color:
                    print("Invalid color or color not found in database")
                    self.setColor()
                else:
                    self.conf.ledStrips[self.strip].setColor(color)
            print("LedStrip on: " +
                "RED "+str(self.conf.ledStrips[self.strip].redPinValue) + 
                ", Green " + str(self.conf.ledStrips[self.strip].greenPinValue) + 
                ", Blue " + str(self.conf.ledStrips[self.strip].bluePinValue))
        if colorVal == "quit":
            self.close()
        elif colorVal == "back":
            self.getLedStripCommand(self.strip)
        else:
            self.getLedStripCommand(self.strip)

    def setFadeIn(self):
        print("[LedStrip"+ str(self.strip) +"] Fading In")
        self.conf.ledStrips[self.strip].fadeIn()
        self.getLedStripCommand(self.strip)

    def setFadeOut(self):
        print("[LedStrip"+ str(self.strip) +"] Fading Out")
        self.conf.ledStrips[self.strip].fadeOut()
        self.getLedStripCommand(self.strip)
    
    def getLightSensorValue(self):
        intensity = self.conf.lightSensor.getLightIntensity()
        print("The sensor is: " + str(intensity))
        self.getLedStripCommand(self.strip)

    def startMotionSensor(self):
        count = 0
        try:
            while True:
                detected = self.conf.motionSensor.detectMotion()
                print("timeTo: " + str(self.timeTo)+", lightsensor at:" + str(self.conf.lightSensor.getLightIntensity()))
                if detected:
                    print("lightsensor at:" + str(self.conf.lightSensor.isNight()))
                    if self.conf.lightSensor.isNight():                    
                        print("strip is " +str(self.conf.ledStrips[self.strip].isOn))
                        if not self.conf.ledStrips[self.strip].isOn:
                            self.conf.ledStrips[self.strip].setColor("#ff0000")
                        self.timeTo += 1000                                     
                        if self.timeTo > 10000:
                            self.timeTo = 10000
                else:                    
                    if self.conf.ledStrips[self.strip].isOn:
                        if self.conf.lightSensor.isDay():
                            print("putting it off")
                            self.timeTo = 10000                            
                            self.conf.ledStrips[self.strip].off()
                        else:
                            self.timeTo -= 100
                            if self.timeTo <= 0:
                                print("putting it off")
                                self.timeTo = 10000                            
                                self.conf.ledStrips[self.strip].off()
                time.sleep(0.1)
        except Exception as e:
            print(e)
            self.close()

    def setIntensity(self):
        intensity = input("[LedStrip"+ str(self.strip) +"] Please select intensity[0-100]: ")
        if not intensity:
            self.getLedStripCommand(self.strip)
        else:
            if intensity == "quit":
                self.close()
            elif intensity == "back":
                self.getLedStripCommand(self.strip)
            else:
                if int(intensity) >-1 and int(intensity) < 101:
                    print("Setting intensity to " + str(intensity))
                    self.conf.ledStrips[self.strip].setIntensity(intensity)
                else:
                    print("invalid number for intensity")
        self.setIntensity()

    def close(self):
        print("[LedStrip"+ str(self.strip) +"] Closing")
        self.conf.ledStrips[self.strip].close()

    def help(self):
        print("Please choose one of the following commands\n" +
            "color: will change the color for the active LedStrip\n" +
            "fadeIn: will fade in the current color\n" +
            "fadeOut: will fade out the current color\n" + 
            "quit: will exist the current menu")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cmd", help = "command to execute")
    parser.add_argument("--color", help = "color to display")
    args = parser.parse_args()
    LedStripController(args)
