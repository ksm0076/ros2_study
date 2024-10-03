# User defined msg Example, Subscribing-Publishing topic

import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

from my_first_package_msgs.msg import CmdAndPoseVel

class CmdAndPose(Node):
    def __init__(self):
        super().__init__('turtle_cmd_pose')
        
        self.sub_pose = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback_pose, 10)
        self.sub_cmdvel = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.callback_cmd, 10)
        # User defined msg
        self.publisher = self.create_publisher(
            CmdAndPoseVel,
            '/cmd_and_pose', 10
        )
        self.cmd_pose = CmdAndPoseVel()
        self.create_timer(1, self.time_callback) # If you want a timer
        
    def callback_pose(self, msg):
        self.cmd_pose.pose_x = msg.x
        self.cmd_pose.pose_y = msg.y
        self.cmd_pose.linear_vel = msg.linear_velocity
        self.cmd_pose.angular_vel = msg.angular_velocity
        
    def callback_cmd(self, msg):
        self.cmd_pose.cmd_vel_linear = msg.linear.x
        self.cmd_pose.cmd_vel_angular = msg.angular.z
    
    def time_callback(self):
        self.publisher.publish(self.cmd_pose)
        print(self.cmd_pose)
        
def main():
    rp.init()
    
    turtle_cmd_pose_node = CmdAndPose()
    rp.spin(turtle_cmd_pose_node)
    
    turtle_cmd_pose_node.destroy_node()
    rp.shutdown()
    
if __name__ == 'main':
    main()