import pigpio as piio
import time

class Test(object):
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        print("getting name")
        return self.__name
    
    @name.setter
    def name(self, value):
        print("setting name")
        self.__name = value
    

if __name__ == "__main__":
    pi = piio.pi("192.168.0.94")
    count = 0
    while count < 100:
        duty = 255 * (count / float(100))
        print("Duty: " + str(duty))
        pi.set_PWM_dutycycle(16,duty)
        count += 1
        time.sleep(0.05)
    time.sleep(5)
    pi.set_PWM_dutycycle(16,0)
