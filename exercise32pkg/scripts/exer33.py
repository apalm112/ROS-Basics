#!/usr/bin/env python

import rospy  # Import the Python library for ROS
# Import the Int32 message from the std_msgs package
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry

# creates a publisher that indicates the age of the robot.
# new msg Age.msg.


def callback(msg):
    print(msg.pose.pose.position.x)


# Initiate a Node called 'topic_subscriber'
rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('/odom', Odometry, callback) # Create a Subscriber object that will listen to the /counter
# topic and will cal the 'callback' function each time it reads
# something from the topic

# Create a loop that will keep the program in execution
rospy.spin()
