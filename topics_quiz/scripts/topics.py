#! /usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

twist_cmd = Twist()
twist_cmd.linear.x = 0.5
twist_cmd.angular.z = 0
distance = 1

def callback(msg):
    if msg.ranges[360] > 1:
        # move forward
        twist_cmd.linear.x = 0.5
        twist_cmd.angular.z = 0
    elif msg.ranges[360] < 1:
        # turn left
        twist_cmd.linear.x = 0.1
        twist_cmd.angular.z = 0.8
    elif msg.ranges[0] < 1:
        # turn left
        twist_cmd.linear.x = 0.1
        twist_cmd.angular.z = 0.8
    elif msg.ranges[719] < 1:
        # turn right
        twist_cmd.linear.x = 0.1
        twist_cmd.angular.z = -0.8

# Initiate a Node named 'topics_quiz_node'
rospy.init_node('topics_quiz_node')
# create publisher that writes to /cmd_vel to move robot
cmd_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=1)
# create a Subscriber that reads from /kobuki/laser/scan topic
laser_subscriber = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rate = rospy.Rate(2)    # Set a publish rate of 2 Hz

while not rospy.is_shutdown():
    cmd_publisher.publish(twist_cmd)
    rate.sleep()