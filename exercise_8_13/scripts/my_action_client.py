#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

# Exercise 8.13

""" Call the action server through the topics and observe the result and feedback.

c) Base your code in the previous Fibonacci example {8.11a} and the client you did in Exercice 7.6 that moved the drone while taking pictures.

The size of the side of the square should be specified in the goal message as an integer.

The feedback should publish the current side (as a number) the robot is at while doing the square.

The result should publish the total number of seconds it took the drone to do the square

Use the _Test.action_ message for that action server. It's msg fields are:
int32 goal
---
int32 result
---
int32 feedback
"""

nSide = 1
DONE = 2

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received


def feedback_callback(feedback):
    global nSide
    print('[Feedback] image n.%d received' % nSide)
    nSide += 1


# initializes the action client node
rospy.init_node('drone_action_client')

# create the connection to the action server
# client = actionlib.SimpleActionClient('/the_action_server_name', the_action_server_message_python_object)
# * First parameter is the name of the action server you want to connecto to.
# * Second parameter is the type of action message that it uses.
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)


cmd_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
drone_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)
drone_land = rospy.Publisher('/drone/land', Empty, queue_size=1)
takeoff = Empty()
landing = Empty()
move_drone = Twist()


# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ArdroneGoal()
# Because the goal message requires to provide the number of seconds taking pictures (in the nseconds variable), you must set that parameter in the goal class instance:
goal.nseconds = 10  # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# Every time a feedback message is received, the feedback_callback function is executed.

# and check for status from time to time
status = client.get_state()
# client.wait_for_result()

while status < DONE:
    drone_takeoff.publish(takeoff)
    move_drone.linear.x = 0.5
    move_drone.angular.z = 0.0
    cmd_publisher.publish(move_drone)
    status = client.get_state()

if status == 3:
    move_drone.linear.x = 0
    move_drone.angular.z = 0
    cmd_publisher.publish(move_drone)
    rospy.sleep(5)
    drone_land.publish(landing)

print('[Result] State: %d' % (client.get_state()))
