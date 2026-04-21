import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomSubscriber(Node):
    def __init__(self):
        super().__init__('odom_subscriber')
        
        # Create a subscriber to the /odom topic
        # It uses the Odometry message type, and a queue size of 10
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)
        
        self.subscription  # Prevent unused variable warning

    def listener_callback(self, msg):
        # Extract the X and Y positions from the nested message structure
        current_x = msg.pose.pose.position.x
        current_y = msg.pose.pose.position.y
        
        # Print out the received message data in a readable format
        self.get_logger().info(f'Received Odom -> Position: X: {current_x:.4f}, Y: {current_y:.4f}')

def main(args=None):
    rclpy.init(args=args)
    node = OdomSubscriber()
    
    try:
        # Keep the node running so it continuously listens to the topic
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        # Clean up and shut down when Ctrl+C is pressed
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
