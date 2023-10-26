import rclpy
from rclpy.action import ActionClient
from shr_msgs.action import DockingRequest

def send_docking_goal():
    rclpy.init()

    try:
        node = rclpy.create_node("docking_client_node")  # Create a node

        action_client = ActionClient(node, DockingRequest, "docking")  # Action client for "docking"

        if not action_client.wait_for_server(timeout_sec=5.0):  # Increased timeout for waiting
            print("Error: Timed out waiting for the docking action server.")
            return

        goal_msg = DockingRequest.Goal()
        # Customize the goal parameters as needed
        # goal_msg.some_field = some_value

        future = action_client.send_goal_async(goal_msg)

        rclpy.spin_until_future_complete(node, future)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    send_docking_goal()
