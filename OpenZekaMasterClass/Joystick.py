from threading import Thread
import time

class Joystick:
    def __init__(self):
        print("you have created a Joystick object")
        self.joystickValues = dict()
        self.joystickValues["rightX"] = 0.0
        self.joystickValues["rightY"] = 0.0
        self.joystickValues["leftX"] = 0.0
        self.joystickValues["leftY"] = 0.0
        self.joystickValues["buttons"] = []

    def startListening(self, frequency):
        self.frequency = frequency
        Thread(target=self.__updateJoystick__, args=()).start()

    def __updateJoystick__(self):
        while True:
            self.joystickValues["rightX"] = 10.0
            self.joystickValues["rightY"] = 10.0
            self.joystickValues["leftX"] = 10.0
            self.joystickValues["leftY"] = 10.0
            self.joystickValues["buttons"] = [5]
            time.sleep(1/self.frequency)
            print("updates joystick every cycle")

    def getJoystick(self):
        return self.joystickValues


