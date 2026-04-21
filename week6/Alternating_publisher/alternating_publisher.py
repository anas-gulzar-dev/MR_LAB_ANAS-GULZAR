import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class AlternatingVelocityPublisher(Node):
    def __init__(self):
        super().__init__('alternating_vel_publisher')
        
        # Create the publisher for the /cmd_vel topic
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Set the timer period to 2 seconds as requested
        timer_period = 2.0 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        # Boolean flag to keep track of the current state
        self.is_moving = False

    def timer_callback(self):
        msg = Twist()
        
        if self.is_moving:
            # State 1: Stop the robot
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Publishing: Zero Velocity (Stopping)')
        else:
            # State 2: Move forward
            msg.linear.x = 0.2  # 0.2 m/s is a safe forward speed for TurtleBot3
            msg.angular.z = 0.0
            self.get_logger().info('Publishing: Forward Velocity (0.2 m/s)')
            
        # Publish the message to the topic
        self.publisher_.publish(msg)
        
        # Toggle the state for the next timer cycle
        self.is_moving = not self.is_moving

def main(args=None):
    rclpy.init(args=args)
    node = AlternatingVelocityPublisher()
    
    try:
        # Spin the node so the timer callback keeps firing
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
