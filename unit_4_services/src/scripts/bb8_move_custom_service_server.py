#! /usr/bin/env python

# ================================================
# Exercise 5.3 
# ================================================

# This new service will be called /move_bb8_in_circle_custom &
# be called thru a custom service message, structure is: int32 duration --- bool success
# bb8 will move for the time int passed in & then STOP

# TODO:

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from unit_4_services.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def my_callback(request):
    print("My_callback in custom_bb8_exercise_5_3 has been called")

    cmd = Twist()
    cmd.linear.x = 0.8
    cmd.angular.z = 0.8

    rate = rospy.Rate(2)   # Set a publish rate of 2 Hz
    count = 0

    while  (count < request.duration):  # Create a loop that will go until someone stops the program execution
        my_publisher.publish(cmd)   # Publish the message within the 'count' variable
        count += 1
        rate.sleep()

    cmd.linear.x = 0.8
    cmd.angular.z = 0.8
    my_publisher.publish(cmd)

    response = MyCustomServiceMessageResponse()
    response.success = True

    return response

rospy.init_node('custom_service_server') 

my_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

my_service = rospy.Service('/move_bb8_in_circle_custom', MyCustomServiceMessage , my_callback) # create the Service called /move_bb8_in_circle with the defined callback
rospy.spin() # maintain the service open.