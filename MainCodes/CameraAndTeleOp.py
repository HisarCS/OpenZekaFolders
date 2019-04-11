#! /usr/bin/env python3
import sys
sys.path.append("..") ## Must be added to include the OpenZeka Class
from OpenZekaMasterClass import ZedCam
from OpenZekaMasterClass import RobotControl
from  OpenZekaMasterClass import RemoteController
from time import sleep
import cv2


camera = ZedCam()
robot = RobotControl()

RC = RemoteController()
RC.startListening()


camera.startLooking()
sleep(1)

camera.startRecording()


while True:
    frame = camera.getImage()
    camera.showFrame()

    lx, ly = RC.getLeftJoystick()
    buttons = RC.getButtons()
    print(buttons, lx, ly)
    robot.setMotorSpeed(ly*100.0)
    robot.setServoAngle(-lx*34.0)
    #sleep(0.05)

    if len(buttons) > 0:
        print("cikiyor")
        camera.stopRecording()

        break



