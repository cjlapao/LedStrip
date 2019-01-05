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
    testObj = Test("Carlos")
    print("t:" + testObj.name)
    testObj.name = "Jorge"
    print("t:" + testObj.name)
