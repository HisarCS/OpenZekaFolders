from threading import Thread
import time

class Lidar:
    def __init__(self):
        print("you have created a Lidar object")

    def startReadingDepth2D(self, range=(-150, 150), frequency=10):
        self.range = range
        self.frequency = frequency

        Thread(target=self.__getDepth2D__, args=()).start()
        time.sleep(0.1)
        print("this should return 2D depth image")

    def getDepth2D(self):
        return self.depthImage

    def __getDepth2D__(self):
        while True:
            self.depthImage = "depth image retriaval"
            time.sleep(1/self.frequency)