#! /usr/bin/env python

import rospkg
import rospy

# Import the service message used by the service /execute_trajectory
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')
# Wait for the service client /execute_trajectory to be running
rospy.wait_for_service('/execute_trajectory')
# Create the connection to the service
traj_by_name_service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
# Create an object of type TrajByNameRequest
traj_by_name_object = ExecTrajRequest()

rospack = rospkg.RosPack()
traj_request_object = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"

# Send through the connection the name of the trajectory to be executed by the robot
result = traj_by_name_service(traj_request_object)
# Print the result given by the service called
print(result)