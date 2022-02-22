#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
import time

# Initiate a Node named 'move_square_publisher'
rospy.init_node('exer21_publisher')
my_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
# Create a Publisher object, that will publish on the /cmd_vel topic
# messages of type Twist
rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz

def move_straight():
    cmd1 = Twist()
    cmd1.linear.x = 0.2
    cmd1.angular.z = 0
    count = 0

    while (count <= 10):
        my_publisher.publish(cmd1)
        count += 1
        rate.sleep()


def stop():
    cmdStop = Twist()
    cmdStop.linear.x = 0
    cmdStop.angular.z = 0
    my_publisher.publish(cmdStop)

def rotater():
    cmdRot = Twist()
    cmdRot.linear.x = 0
    cmdRot.angular.z = 0.55
    count = 0

    while (count <= 5):
        my_publisher.publish(cmdRot)
        count += 1
        rate.sleep()

move_straight()
stop()
rotater()
stop()
move_straight()
stop()
rotater()
stop()
move_straight()
stop()
rotater()
stop()
move_straight()
stop()
rotater()
stop()