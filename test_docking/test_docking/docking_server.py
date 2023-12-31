import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from test_docking.docking_main import Docking
from shr_msgs.action import DockingRequest

class DockingActionServer(Node):
    
    def __init__(self):
        super().__init__('Docking_action_server')
        self.docking = Docking()   
        
        self.action_server = ActionServer(
            self,
            DockingRequest,  # Replace with the actual action type
            'docking',
            execute_callback=self.execute_callback
        )
        #print("working action")
    def execute_callback(self, goal_handle):
        print("working callback")
        print("working init", goal_handle)

        while not self.docking.bumped:
            self.docking.get_transformation_from_aptag_to_port()
            self.docking.move_towards_tag()
            
        print(self.docking.bumped)
        if self.docking.bumped:
            print("Bumped!!")
            goal_handle.succeed()
            result = DockingRequest.Result()
            result.result = True
            self.docking.bumped = False
            return result
        else:
            goal_handle.abort()
            result = DockingRequest.Result()
            result.result = False
            return result
	

def main(args=None):
    rclpy.init(args=args)
    subscriber_node = DockingActionServer()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
