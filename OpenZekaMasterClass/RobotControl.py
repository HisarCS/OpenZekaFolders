

class RobotControl:
    def __init__(self):
        print("you have created a RobotControl object")

    def setMotorSpeed(self, speed=0):
        self.speed = speed
        print("set motor speed to:{}".format(self.speed))

    def setServoAngle(self, desiredAngle=0):
        self.desiredAngle = desiredAngle
        print("set desired angle to:{}".format(self.desiredAngle))
