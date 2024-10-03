import rclpy as rp
from rclpy.node import Node

from my_first_package_msgs.srv import MultiSpawn
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import Spawn

import random

class NSpawning(Node):
    def __init__(self):
        super().__init__('multi_spawn')
        self.server = self.create_service(
            MultiSpawn,
            'multi_spawn2',
            self.callback_service
        )
        self.spawn = self.create_client(Spawn, '/spawn')
        self.req_spawn = Spawn.Request()
        
    
    def callback_service(self, request, response):
        print("You request", request.num , "turtles")
        for n in range(request.num):
            
            self.req_spawn.x = float(random.randrange(1,8))
            response.x.append(self.req_spawn.x)
            self.req_spawn.y = float(random.randrange(1,8))
            response.y.append(self.req_spawn.y)
            self.spawn.call_async(self.req_spawn)
        return response
        
def main():
    print("HELLO~")
    rp.init()
    multi_spawn = NSpawning()
    
    rp.spin(multi_spawn)
    rp.shutdown()

if __name__ == 'main':
    main()