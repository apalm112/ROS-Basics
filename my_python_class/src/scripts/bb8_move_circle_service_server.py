#! /usr/bin/env python

import rospy
from my_python_class.srv import MoveCircleServiceMessage, MoveCircleServiceMessageResponse 
from bb8_move_circle_class import MoveBB8

# ====================================
# Exercise Unit 6
# ====================================


def my_callback(request):
    rospy.loginfo("The Service move_bb8_in_circle has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8(request.duration)
    rospy.loginfo("Finished service move_bb8_in_circle")
    my_response = MoveCircleServiceMessageResponse()
    my_response.success = True
    return my_response 

rospy.init_node("service_move_bb8_in_circle_server") 
my_service = rospy.Service("/move_bb8_in_circle", MoveCircleServiceMessage , my_callback)
rospy.loginfo(" Service \n /move_bb8_in_circle \n is Ready...")
rospy.spin()