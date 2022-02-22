#! /usr/bin/env python

# ================================================
# Exercise 5.2 Re-Do
# ================================================

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.

def my_callback(request):
    print("My_callback in bb8 unit_5_pkg has been called")
    cmd = Twist()
    cmd.linear.x = 0.8
    cmd.angular.z = 0.8
    rate = rospy.Rate(2)
    count = Int32()        
    count.data = 0

    while not rospy.is_shutdown():
        my_publisher.publish(cmd)   # Publish the message within the 'count' variable
        count.data += 1 
        rate.sleep()

    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 

rospy.init_node('service_server') 

my_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

my_service = rospy.Service('/move_bb8_in_circle', Empty , my_callback) # create the Service called /move_bb8_in_circle with the defined callback
rospy.spin() # maintain the service open.