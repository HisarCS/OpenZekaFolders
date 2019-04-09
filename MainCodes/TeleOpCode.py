from  import RobotControl
from  OpenZekaMasterClass import RemoteController
from time import sleep

RC = RemoteController()
RC.startListening()

robot = RobotControl()

while True:
    lx, ly = RC.getLeftJoystick()
    robot.setMotorSpeed(ly*100.0)
    robot.setServoAngle(-lx*34)
    sleep(0.05)
