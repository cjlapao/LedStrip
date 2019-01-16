import RPi.GPIO as GPIO
import pigpio as piio
import time
from Color import Color
from settings.LedStripSettings import LedStripSettings

class LedStrip(object):
    
    def __init__(self, settings):
        self.isOn = False
        self.__settings = LedStripSettings
        self.__settings = settings
        self.__color = Color()

        self.__color = self.__settings.currentColor
        self.__redPin = self.__settings.redPin
        self.__greenPin = self.__settings.greenPin
        self.__bluePin = self.__settings.bluePin
        self.__intensity = 100


        self.__redPinValue = 0
        self.__greenPinValue = 0
        self.__bluePinValue = 0
        self.__name = "none"

        self.__pwmR = None
        self.__pwmG = None
        self.__pwmB = None

        self.__steps = 50
        self.__duration = 2
        self.setupGPIO()
    
    def setupGPIO(self):
        print("Setting up Rpi GPIO")
        self.__pi = piio.pi()
        self.__startPWM()        
        print("GPIO setup finished...")

    def __startPWM(self):
        print("GPIO PWM started")
    
    def __stopPWM(self):
        #GPIO.cleanup()
        self.__pi.set_PWM_dutycycle(self.redPin, 0)
        self.__pi.set_PWM_dutycycle(self.greenPin, 0)
        self.__pi.set_PWM_dutycycle(self.bluePin, 0)
        self.__pi.stop()
        self.isOn = False
        print("GPIO PWM stopped...")
    
    def off(self):
        self.setColor("#010101")     
        self.isOn = False

    def __restartPWM(self):
        self.__stopPWM()
        self.__startPWM()

    def setColor(self, name, intensity = 100):
        self.color.fromHex(name)
        self.redPinValue = self.color.red
        self.greenPinValue = self.color.green
        self.bluePinValue = self.color.blue
        if self.color.red == 0 and self.color.green == 0 and self.color.blue == 0:
            self.isOn = False
            self.close()
        else:
            redPwm = self.redPinValue / float(255) * 255
            greenPwm = self.greenPinValue / float(255) * 255
            bluePwm = self.bluePinValue / float(255) * 255
            #print("redPwm:" + str(redPwm) + " greenPwm:" + str(greenPwm) +  " bluePwm:" + str(bluePwm))
            self.__pi.set_PWM_dutycycle(self.redPin, redPwm)
            self.__pi.set_PWM_dutycycle(self.greenPin, greenPwm)
            self.__pi.set_PWM_dutycycle(self.bluePin, bluePwm)
            self.__intensity = 100
            self.isOn = True
            #print("LedStrip color updated...")

    def setIntensity(self, intensity):
        try:
            intensity = int(intensity)
        except:
            intensity = 100 
            pass
        self.__intensity = intensity
        color = Color()
        color.fromHex(self.__color.toHex())
        color.darken(100 - intensity)
        if color.red == 0 and color.green == 0 and color.blue == 0:
            self.isOn = False
            self.close()
        self.__pi.set_PWM_dutycycle(self.redPin, color.red)
        self.__pi.set_PWM_dutycycle(self.greenPin, color.green)
        self.__pi.set_PWM_dutycycle(self.bluePin, color.blue)
        print("LedStrip color intensity updated...")
        self.isOn = True

    def close(self):
        self.__stopPWM()
    
    def fadeOut(self):
        if self.isOn:
            count = 0
            intensity = (100 / self.__steps)
            duration = int(self.__duration * 1000)
            newIntensity =  0
            oldColor = Color()
            oldColor.fromHex(self.__color.toHex())
            while count < self.__steps:
                count += 1
                newIntensity += intensity
                newColor = oldColor.getDarkerVersion(newIntensity)
                self.setColor(newColor)
                time.sleep((1 * duration / self.__steps) / 1000)
            self.setColor("#010101")
            self.__color.fromHex(oldColor.toHex())
            self.isOn = False

    def fadeIn(self):
        if not self.isOn:
            count = 0
            intensity = (100 / self.__steps)
            duration = int(self.__duration * 1000)
            newIntensity =  100
            oldColor = Color()
            oldColor.fromHex(self.__color.toHex())
            while count < self.__steps:
                count += 1
                newIntensity -= intensity
                newColor = oldColor.getDarkerVersion(newIntensity)
                self.setColor(newColor)
                time.sleep((1 * duration / self.__steps) / 1000)
            self.__color.fromHex(oldColor.toHex())
            self.setColor(self.__color.toHex())
            self.isOn = True

    def __getname(self):
        return self.__name

    def __setname(self, name):
        self.__name = name + "Settted"

    def __getredPin(self):
        return self.__redPin
    
    def __setredPin(self, value):
        self.__redPin = value
    
    def _get_greenPin(self):
        return self.__greenPin
    
    def _set_greenPin(self, value):
        self.__greenPin = value
    
    def _get_bluePin(self):
        return self.__bluePin
    
    def _set_bluePin(self, value):
        self.__bluePin = value

    def __getredPinValue(self):
        return self.__redPinValue
    
    def __setredPinValue(self, value):
        self.__redPinValue = value

    def _get_greenPinValue(self):
        return self.__greenPinValue
    
    def _set_greenPinValue(self, value):
        self.__greenPinValue = value

    def _get_bluePinValue(self):
        return self.__bluePinValue
    
    def _set_bluePinValue(self, value):
        self.__bluePinValue = value
    
    def __getIntensity(self):
        return self.__intensity

    def __setIntensity(self, value):
        self.setIntensity(value)
    
    def __getDuration(self):
        return self.__duration
    
    def __setDuration(self, value):
        self.__duration = value

    def __getSteps(self):
        return self.__steps
    
    def __setSteps(self, value):
        self.__steps = value
    
    def __getIsOn(self):
        return self.__isOn
    
    def __setIsOn(self, value):
        self.__isOn = value

    def __getColor(self):
        return self.__color

    def __setColor(self, value):
        self.__color = value

    name = property(__getname, __setname)

    redPin = property(__getredPin, __setredPin)

    redPinValue = property(__getredPinValue, __setredPinValue)

    greenPin = property(_get_greenPin, _set_greenPin)

    greenPinValue = property(_get_greenPinValue, _set_greenPinValue)

    bluePin = property(_get_bluePin, _set_bluePin)

    bluePinValue = property(_get_bluePinValue, _set_bluePinValue)

    duration = property(__getDuration, __setDuration)

    intensity = property(__getIntensity, __setIntensity)

    steps = property(__getSteps, __setSteps)

    isOn = property(__getIsOn, __setIsOn)

    color = property(__getColor, __setColor)