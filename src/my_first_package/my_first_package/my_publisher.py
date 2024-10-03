import rclpy as rp
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtlesimPublisher(Node):
    def __init__(self):
        super().__init__('turtlesim_publisher') # node nmae
        
        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10)
        self.create_timer(1.5, self.time_callback) # If you want a timer   
        
    def time_callback(self):
        msg = Twist()
        msg.linear.x = 1.0        
        msg.linear.y = 1.0
        msg.angular.z = 1.0
        self.publisher.publish(msg)
            
def main():
    rp.init()
    
    turtlesim_publisher = TurtlesimPublisher()    
    rp.spin(turtlesim_publisher)
    
    turtlesim_publisher.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()