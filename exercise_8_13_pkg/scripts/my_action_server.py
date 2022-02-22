# #! /usr/bin/env python
# import rospy
# import actionlib
# from actionlib.msg import TestActionGoal, TestActionFeedback, TestActionResult
# from geometry_msgs.msg import Twist
# from std_msgs.msg import Empty

# """ 
#     THIS DOES NOT WORK, YET..............
#  """


# class SquareClass(object):
    
#   # create messages that are used to publish feedback/result
#   _feedback = TestActionFeedback()
#   _result   = TestActionResult()

#   def __init__(self):
#     # creates the action server
#     self._as = actionlib.SimpleActionServer("move_as", TestActionGoal, self.goal_callback, False)
#     self._as.start()
    
#   def goal_callback(self, goal):
#     # this callback is called when the action server is called.
#     # and returns the sequence to the node that called the action server
    
#     # helper variables
#     r = rospy.Rate(1)
#     success = True
#     self.my_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
#     self.takeoff_publisher = rospy.Publisher('ardrone/takeoff', Empty, queue_size=1)
#     self.takeoff = Empty()
#     self.land_publisher = rospy.Publisher('ardrone/land', Empty, queue_size=1)
#     self.land = Empty()
#     self.ardrone_move = Twist()
#     self.x = 0.3
#     self.z = 0.3
#     self.count = 1
#     self.square = 2
    
#     _x = rospy.get_rostime()
#     SquareOrder = self.count

#     while SquareOrder > 0:
#         if self._as.is_preempt_requested():
#             rospy.loginfo('The goal has been preempted.')
#             self._as.set_preempted()
#             success = False
#             break

#         # move = square
#         move = self.square
#         self._feedback.feedback = 1
#         while move > 0:
#             _count = goal.goal
#             while _count > 0:
#                 self.takeoff_publisher(self.takeoff)
#                 self.ardrone_move.linear.x = self.x
#                 self.my_publisher(self.ardrone_move)
#                 rospy.sleep(1)
#                 self._as.publish_feedback(self._feedback)
#                 _count -= 1

#             _count = goal.goal
#             self._feedback.feedback += 1
#             while _count > 0:
#                 self.ardrone_move.linear.y = self.y
#                 self.ardrone_move.linear.x = 0
#                 self.my_publisher.publish(self.ardrone_move)
#                 rospy.sleep(1)
#                 _count -= 1

#             self._feedback.feedback += 1
#             self.ardrone_move.linear.y = 0
#             self.my_publisher.publish(self.ardrone_move)
#             self.x = -self.x
#             self.y = -self.y
#         SquareOrder -= 1
#         print('Square', SquareOrder)
    
#     self.ardrone_move.linear.x = 0
#     self.ardrone_move.angular.z = 0
#     self.my_publisher.publish(self.ardrone_move)
#     self.land_publisher.publish(self.land)
    
#     # at this point, either the goal has been achieved (success==true)
#     # or the client preempted the goal (success==false)
#     # If success, then we publish the final result
#     # If not success, we do not publish anything in the result
#     if success:
#       self._result.result = self._feedback.feedback * 2 * self.square
#       rospy.loginfo('Time drone was moving %d' % self._result.result )
#       self._as.set_succeeded(self._result)
      
# if __name__ == '__main__':
#   rospy.init_node('my_action_server')
#   SquareClass()
#   rospy.spin()