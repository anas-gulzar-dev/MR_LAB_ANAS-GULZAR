import rclpy
from rclpy.node import Node


class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        self.get_logger().info('Welcome to Mobile Robotics Lab')
        # Counter logic
        import os
        counter_file = os.path.join(os.path.dirname(__file__), 'run_count.txt')
        try:
            with open(counter_file, 'r') as f:
                count = int(f.read().strip())
        except (FileNotFoundError, ValueError):
            count = 0
        count += 1
        with open(counter_file, 'w') as f:
            f.write(str(count))
        self.get_logger().info(f'Run count: {count}')

        # Task 3: Print student_name parameter
        self.declare_parameter('student_name', None)
        student_name = self.get_parameter('student_name').get_parameter_value().string_value
        if student_name:
            self.get_logger().info(f'student_name: {student_name}')
        else:
            self.get_logger().info('student_name not set')


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()

    # spin_once lets us create the node, log once, and exit cleanly
    rclpy.spin_once(node, timeout_sec=0.1)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
