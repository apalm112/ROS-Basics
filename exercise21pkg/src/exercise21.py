#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

# Initiate a Node named 'topic_publisher'
rospy.init_node('exer21_publisher')
my_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
# Create a Publisher object, that will publish on the /cmd_vel topic
# messages of type Twist

cmd = Twist()
cmd.linear.x = 0.8
cmd.angular.z = 0.8

rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
count = Int32()                            # Create a var of type Int32
count.data = 0

while not rospy.is_shutdown():             # Create a loop that will go until someone stops the program execution
    # Publish the message within the 'count' variable
    my_publisher.publish(cmd)
    count.data += 1                          # Increment 'count' variable
    rate.sleep()
