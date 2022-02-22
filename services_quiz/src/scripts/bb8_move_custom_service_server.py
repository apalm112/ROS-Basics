#! /usr/bin/env python

import rospy
import time
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist
from services_quiz.srv import BB8CustomServiceMessage, BB8CustomServiceMessageResponse

""" 
use data passed to new service to make robot move in square
must repeat based on the repetitions variable
return True if all went OK via success variable
"""

cmd = Twist()

def move_straight(side):
    cmd.linear.x = 1.0
    cmd.angular.z = 0
    count= 1
    while (count < side):
        my_publisher.publish(cmd)
        count += 1
        rate.sleep()
    stop()

def turn(repetitions):
    cmd.linear.x = 0
    cmd.angular.z = 1.1
    count = 0
    while (count < repetitions):
        my_publisher.publish(cmd)
        count += 1
        rate.sleep()
    stop()

def stop():
    #rospy.loginfo("shutdown time! Stop the robot")
    cmd.linear.x = 0.0
    cmd.angular.z = 0.0
    my_publisher.publish(cmd)

def move_in_square(side, repetitions):
    for idx in range(4):
        move_straight(side)
        turn(repetitions)

def my_callback(request):
    print("My_callback in services_quiz has been called")
    move_in_square(request.side, request.repetitions)
    rate.sleep()

    # count = 1
    # while (count <= request.repetitions):
    #     move_in_square(request.side, request.repetitions)
    #     # turn(request.repetitions)
    #     count += 1
    #     # print("COUNT:", count, "request.duration:", request.side)
    #     rate.sleep()
    # stop()
    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('custom_service_server') 
rate = rospy.Rate(2)

my_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
# create the Service called /move_bb8_in_square_custom with the defined callback
my_service = rospy.Service('/move_bb8_in_square_custom', BB8CustomServiceMessage , my_callback)

rospy.spin() # maintain the service open