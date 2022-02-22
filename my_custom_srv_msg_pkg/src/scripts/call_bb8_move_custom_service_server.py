#! /usr/bin/env python

# ================================================
# Exercise 5.3 It WORKS!
# ================================================

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

# calls the service /move_bb8_in_circle_custom
rospy.init_node('service_client')
rospy.wait_for_service('/move_bb8_in_circle_custom')
service_client = rospy.ServiceProxy('/move_bb8_in_circle_custom')
request_object = MyCustomServiceMessage()

result = service_client(request_object)
print(result)
# rospy.spin() # maintain the service open