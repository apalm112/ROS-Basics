#! /usr/bin/env python

# ================================================
# Exercise 5.2 Re-Do
# ================================================

import rospkg
import rospy
from std_srvs.srv import Empty, EmptyRequest

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /move_bb8_in_circle to be running
rospy.wait_for_service('/move_bb8_in_circle')
# Create the connection to the service
bb8_service_client = rospy.ServiceProxy('/move_bb8_in_circle', Empty)
bb8_request_object = EmptyRequest()

# Send through the connection the name of the trajectory to be executed by the robot
result = bb8_service_client(bb8_request_object)
# Print the result given by the service called
print(result)

# Node: /bb8_move_in_circle_service_server
# Type: std_srvs/Empty