import sys
sys.path.append("..")

from OpenZekaMasterClass import RobotControl
from  OpenZekaMasterClass import RemoteController
from time import sleep

RC = RemoteController()
RC.startListening()

robot = RobotControl()

while True:
    lx, ly = RC.getLeftJoystick()
    print(lx, ly)
    robot.setMotorSpeed(ly*100.0)
    robot.setServoAngle(-lx*34.0)
