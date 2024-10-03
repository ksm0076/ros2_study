import rclpy as rp
from rclpy.node import Node
from my_first_package_msgs.srv import MultiSpawn
from turtlesim.srv import TeleportAbsolute

import random

class MultiSpawning(Node):
    def __init__(self):
        super().__init__('multi_spawn')
        self.server = self.create_service(
            MultiSpawn,
            'multi_spawn',
            self.callback_service
        )
        self.teleport = self.create_client(
            TeleportAbsolute,
            '/turtle1/teleport_absolute'
        )
        self.req_teleport = TeleportAbsolute.Request()
        
    def callback_service(self, request, response):
        # print("Request: ", request)
        
        # response.x = [1., 2., 3.]
        # response.y = [10., 20.]
        # response.theta = [100., 200., 300.]
        
        self.req_teleport.x = float(random.randrange(1,8))
        self.teleport.call_async(self.req_teleport)
        print("Hello~~@~@~@~@~@")
        return response

def main():
    rp.init()
    multi_spawn = MultiSpawning()
    
    rp.spin(multi_spawn)
    rp.shutdown()

if __name__ == 'main':
    main()