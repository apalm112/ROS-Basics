#! /usr/bin/env python

import rospy  # Import the Python library for ROS
# Import the Int32 message from the std_msgs package
from std_msgs.msg import Int32
from nav_msgs.msg import Odometry

def callback(msg):
    print(msg.data)

rospy.init_node('topic_subscriber') # Initiate a Node called 'topic_subscriber'
sub = rospy.Subscriber('/counter', Int32, callback) # Create a Subscriber object that will listen to the /counter
 # topic and will cal the 'callback' function each time it reads something from the topic
rospy.spin()  # Create a loop that will keep the program in execution

#   $ rostopic info /counter
#     Type: std_msgs/Int32