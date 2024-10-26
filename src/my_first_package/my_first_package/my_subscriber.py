import rclpy as rp
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtlesimSubscriber(Node):
    def __init__(self):
        super().__init__('turtlesim_subscriberr') # node nmae
        self.x = None
        self.y = None
        
        self.subscribtion = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback,
            10)
        self.create_timer(1, self.time_callback) # If you want a timer
    
    def callback(self, msg):        
        self.x = msg.x
        self.y = msg.y
        
    def time_callback(self):
        print("XX: ", self.x, "YY: ", self.y)
        
            
def main():
    rp.init()
    
    turtlesim_subscriber = TurtlesimSubscriber()    
    rp.spin(turtlesim_subscriber)
    
    turtlesim_subscriber.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()