import rclpy as rp
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute

import random

class ClientTest(Node):
    def __init__(self):
        super().__init__('client_test')
        self.teleport = self.create_client(
            TeleportAbsolute,
            '/turtle1/teleport_absolute'
        )
        self.req_teleport = TeleportAbsolute.Request() # request type
        self.create_timer(1, self.callback_service)
        
    def callback_service(self):        
        self.req_teleport.x = float(random.randrange(1,8))
        self.teleport.call_async(self.req_teleport)
        print("Client Test")
    
def main():
    rp.init()
    client_node = ClientTest()
    
    rp.spin(client_node)
    rp.shutdown()

if __name__ == 'main':
    main()