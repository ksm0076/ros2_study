import rclpy as rp
from rclpy.node import Node
from rclpy.action import ActionServer

from my_first_package_msgs.action import DisTurtle

import time

class DistTurtleServer(Node):
    def __init__(self):
        super().__init__('dist_turtle_action_server')
        self.action_server = ActionServer(
            self,
            DisTurtle,
            'dist_turtle',
            self.execute_callback
        )
    def execute_callback(self, goal_handle):
        feedback_msg = DisTurtle.Feedback()
        for n in range(10):
            feedback_msg.remained_dist = float(n)
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)
        goal_handle.succeed()
        result = DisTurtle.Result()
        return result
    
def main():
    print("Activating: my_action_server")
    rp.init()
    dist_turtle_action_server = DistTurtleServer()
    
    rp.spin(dist_turtle_action_server)
    rp.shutdown()

if __name__ == 'main':
    main()