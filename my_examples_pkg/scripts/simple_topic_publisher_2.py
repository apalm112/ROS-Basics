#! /usr/bin/env python

import rospy
from std_msgs.msg import Int32 

# Exercise 9.3

def callback(msg): 
    print (msg.data)

rospy.init_node('topic_publisher')
pub = rospy.Publisher('/counter', Int32, queue_size=1)

sub = rospy.Subscriber('/topic_subscriber', Int32, callback)

rate = rospy.Rate(2)
count = Int32()
count.data = 0

while not rospy.is_shutdown(): 
  pub.publish(count)
  count.data += 1
  rate.sleep()

rospy.spin()