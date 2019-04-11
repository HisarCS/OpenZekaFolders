#! /usr/bin/env python3

import subprocess
_ = subprocess.Popen(['cd', '/home/nvidia/racecar-ws/', '&', 'roslaunch', 'racecar', 'teleop2.launch'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from threading import Thread
from time import sleep


class RobotControl:
    def __init__(self, controlFreq=100):
        # print("you have created a RobotControl object")
        self.controlFreq = controlFreq
        rospy.init_node("RobotControl")
        self.pub = rospy.Publisher("/ackermann_cmd", AckermannDriveStamped, queue_size=1)
        self.rate = rospy.Rate(self.controlFreq)
        self.moveMotors = AckermannDriveStamped()

        self.stopEverything()
        self.isUpdating = True

        Thread(target=self.__update__, args=()).start()

    def stopEverything(self):
        self.moveMotors.drive.speed = 0.0
        self.moveMotors.drive.steering_angle = 0.0

    def __update__(self):
        while (not rospy.is_shutdown()) and (self.isUpdating):
            self.pub.publish(self.moveMotors)
            self.rate.sleep()

    def close(self):
        self.isUpdating = False


    def setMotorSpeed(self, speed):

        100.0 if speed>100.0 else speed
        -100.0 if speed < -100.0 else speed

        self.speed = speed/50.0
        # print("set motor speed to:{}".format(self.speed))
        self.moveMotors.drive.speed = self.speed


    def setServoAngle(self, desiredAngle):

        34.0 if desiredAngle > 34.0 else desiredAngle
        -34.0 if desiredAngle < -34.0 else desiredAngle

        self.desiredAngle = desiredAngle/100.0
        self.moveMotors.drive.steering_angle = self.desiredAngle
        # print("set desired angle to:{}".format(self.desiredAngle))



