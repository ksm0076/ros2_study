import rclpy as rp
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from rclpy.action import ActionServer

from my_first_package.my_subscriber import TurtlesimSubscriber
from my_first_package_msgs.action import DisTurtle
from rclpy.executors import MultiThreadedExecutor

import math
import time

class DistTurtleServer(Node):
    def __init__(self):
        super().__init__('move_turtle_action_server')
        self.total_dist = 0
        self.is_first_time = True
        self.current_pose = Pose()
        self.previous_pose = Pose()
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.action_server = ActionServer(
            self,
            DisTurtle,
            'move_turtle',
            self.execute_callback
        )
        print("Go distance!!")
        self.get_logger().info("Go distance!!")
    def execute_callback(self, goal_handle):
        feedback_msg = DisTurtle.Feedback()
        
        msg = Twist()
        msg.linear.x = goal_handle.request.linear_x
        msg.angular.z = goal_handle.request.angular_z
        
        while True:
            self.total_dist += self.calc_move_dist()
            feedback_msg.remained_dist = goal_handle.request.dist - self.total_dist
            goal_handle.publish_feedback(feedback_msg)
            self.publisher.publish(msg)
            time.sleep(1)
            
            if feedback_msg.remained_dist < 0.2:
                break
        
        goal_handle.succeed()
        result = DisTurtle.Result()
        
        result.pos_x = self.current_pose.x
        result.pos_y = self.current_pose.y
        result.pos_theta = self.current_pose.theta
        result.result_dist = self.total_dist
        
        self.total_dist = 0
        self.is_first_time = True
        
        return result
    
    def calc_move_dist(self):
        if self.is_first_time:
            self.previous_pose.x = self.current_pose.x
            self.previous_pose.y = self.current_pose.y
            self.is_first_time = False
        move_dist = math.sqrt((self.current_pose.x - self.previous_pose.x)**2
                              + (self.current_pose.y - self.previous_pose.y)**2)
        self.previous_pose = self.current_pose
        return move_dist
    
class TurtleSub_Action(TurtlesimSubscriber):
    def __init__(self, ac_server):
        super().__init__()
        self.ac_server = ac_server
    def callback(self, msg):        
        self.x = msg.x
        self.y = msg.y
        self.ac_server.current_pose = msg
    
def main():
    rp.init()
    
    executor = MultiThreadedExecutor()
    
    ac = DistTurtleServer()
    sub = TurtleSub_Action(ac)
    
    executor.add_node(sub)
    executor.add_node(ac)
    
    try:
        executor.spin()
    finally:
        executor.shutdown()
        sub.destroy_node()
        ac.destroy_node()
        rp.shutdown()