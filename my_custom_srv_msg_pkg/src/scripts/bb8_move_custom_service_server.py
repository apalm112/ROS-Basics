#! /usr/bin/env python

# ================================================
# Exercise 5.3  THIS ONE WORKS!
# ================================================

# This new service will be called /move_bb8_in_circle_custom
# & be called thru a custom service message MyCustomServiceMessage.srv, 
# structure is: 
#   int32 duration 
#   --- 
#   bool success
# bb8 will move for the time int passed in & then STOP

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

cmd = Twist()
cmd.linear.x = 0.9
cmd.angular.z = 0.8
# print('TYPE:', type(request.duration))

def stop():
    cmd.linear.x = 0.0
    cmd.angular.z = 0.0
    my_publisher.publish(cmd)

def my_callback(request):
    print("My_callback in my_custom_srv_msg_pkg has been called")
    rate = rospy.Rate(2)
    count = 0
    while (count <= request.duration):
        my_publisher.publish(cmd)
        count += 1
        print("COUNT:", count, "request.duration:", request.duration)
        rate.sleep()
    stop()
    response = MyCustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('custom_service_server') 

my_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
# create the Service called /move_bb8_in_circle_custom with the defined callback
my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback)
rospy.spin() # maintain the service open.