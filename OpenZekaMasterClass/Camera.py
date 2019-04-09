from threading import Thread



class Camera:
    def __init__(self):
        print("you have created a Camera object")

    def startGettingFrames(self, onlyTheseFrames=("FrontRight", "FrontLeft", "Back")):
        self.framesToBeQueued = onlyTheseFrames
        print(self.framesToBeQueued)
        Thread(target=self.__frameUpdater__, args=()).start()


    def __getFrontRight__(self):
        self.frontRightCamera = "frontRightCamera"
        print("reveives only FrontRight camera")

    def __getFrontLeft__(self):
        self.frontLeftCamera = "frontLeftCamera"
        print("reveives only FrontLeft camera")

    def __getBack__(self):
        self.backCamera = "backCamera"
        print("reveives only Back camera")

    def __frameUpdater__(self):
        while True:
            for frame in self.framesToBeQueued:
                if frame == "FrontRight":
                    self.__getFrontRight__()
                elif frame == "FrontLeft":
                    self.__getFrontLeft__()
                elif frame == "Back":
                    self.__getBack__()

