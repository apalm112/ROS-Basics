#! /usr/bin/env python
import rospy
import time
import actionlib
from ardrone_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult, ArdroneFeedback

# Exercise 7.4a
# TODO:
# Create a package that contains and launches the action client from Exercise {7.4a}: ardrone_action_client.py, from a launch file.
# Add some code that makes the quadcopter move around while the action server has been called (in order to take pictures while the robot is moving).
# Stop the movement of the quadcopter when the last picture has been taken (action server has finished).

""" 1) You can send Twist commands to the quadcopter in order to move it. These commands have to be published in /cmd_vel topic. Remember the Topics Units.

2) You must send movement commands while waiting until the result is received, creating a loop that sends commands at the same time that check for completion. In order to be able to send commands while the action is in progress, you need to use the SimpleActionClient function get_state().

3) Also, take into account that in some cases, the 1st message published into a topic may fail (because the topic connections are not ready yet). It's important to bear this in mind specially for taking off/landing the drone, since it's based in a single publication into the corresponding topics. Have a look at this post for more information about this. """

nImage = 1

# definition of the feedback callback. This will be called when feedback
# is received from the action server
# it just prints a message indicating a new message has been received
def feedback_callback(feedback):
    global nImage
    print('[Feedback] image n.%d received'%nImage)
    nImage += 1

# initializes the action client node
rospy.init_node('drone_action_client')

# create the connection to the action server
# client = actionlib.SimpleActionClient('/the_action_server_name', the_action_server_message_python_object)
# * First parameter is the name of the action server you want to connecto to.
# * Second parameter is the type of action message that it uses. 
client = actionlib.SimpleActionClient('/ardrone_action_server', ArdroneAction)
# waits until the action server is up and running
client.wait_for_server()

# creates a goal to send to the action server
goal = ArdroneGoal()
# Because the goal message requires to provide the number of seconds taking pictures (in the nseconds variable), you must set that parameter in the goal class instance:
goal.nseconds = 10 # indicates, take pictures along 10 seconds

# sends the goal to the action server, specifying which feedback function
# to call when feedback received
client.send_goal(goal, feedback_cb=feedback_callback)

# Every time a feedback message is received, the feedback_callback function is executed.

# Uncomment these lines to test goal preemption:
#time.sleep(3.0)
#client.cancel_goal()  # would cancel the goal 3 seconds after starting

# wait until the result is obtained
# you can do other stuff here instead of waiting
# and check for status from time to time 
# status = client.get_state()
# check the client API link below for more info

client.wait_for_result()

print('[Result] State: %d'%(client.get_state()))