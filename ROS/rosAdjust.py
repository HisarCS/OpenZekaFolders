import rosbag
import rosmsg
from datetime import datetime
from time import time


class Ros_Adjust:
    def __init__(self):
    	self.bag = rosbag.Bag('otayfinalV1.bag')
    	self.output_bag = rosbag.Bag('output.bag', 'w')


    def adjust_data_by_vel_and_acc(self):
        #print(self.bag.get_type_and_topic_info().topics)
        for self.topic, self.msg, self.t in self.bag.read_messages():
            if (self.msg.drive.speed != 0 or self.msg.drive.acceleration != 0 or self.msg.drive.steering_angle != 0):
                self.output_bag.write(self.topic, self.msg, self.t)


    def split_data(self):
        time1 = time()
        for self.topic, self.msg, self.t in self.bag.read_messages():
            if (abs(time1 - time())<8.0):
                self.output_bag.write(self.topic, self.msg, self.t)


Adjust =Ros_Adjust()
Adjust.split_data()
