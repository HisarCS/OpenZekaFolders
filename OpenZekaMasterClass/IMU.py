from threading import Thread
import time

class IMU:
    def __init__(self):
        print("you have created an IMU object")
        self.angle = 0.0

    def startListrening(self, frequency):
        self.frequency = frequency
        Thread(target=self.__updateIMU__, args=()).start()

    def __updateIMU__(self):
        while True:
            print("updates IMU every cycle")
            self.angle = 10.0
            time.sleep(1/self.frequency)

    def getAngle(self):
        return self.angle
