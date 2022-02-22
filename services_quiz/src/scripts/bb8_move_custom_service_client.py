#! /usr/bin/env python

import rospkg
import rospy
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest

rospy.init_node('move_bb8_in_square_custom_client')
rospy.wait_for_service('move_bb8_in_square_custom')
service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage)
request_object = BB8CustomServiceMessageRequest()

request_object.side = 2
request_object.repetitions = 2

rospy.loginfo("Start Two Small Squares...")
result = service_client(request_object)

request_object.side = 4
request_object.repetitions = 1

rospy.loginfo("Start One Big Square...")
result = service_client(request_object)

rospy.loginfo("END of Service call...")