#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from turtlesim.msg import Pose


class MoveToGoal(Node):
    def __init__(self) -> None:
        super().__init__('move_to_goal')

        self.declare_parameter('target_x', 8.0)
        self.declare_parameter('target_y', 8.0)
        self.target_x = self.get_parameter('target_x').get_parameter_value().double_value
        self.target_y = self.get_parameter('target_y').get_parameter_value().double_value

        self.current_pose = None
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.control_loop)

        self.get_logger().info(f'Moving turtle1 to ({self.target_x:.2f}, {self.target_y:.2f})')

    def pose_callback(self, message: Pose) -> None:
        self.current_pose = message

    def control_loop(self) -> None:
        if self.current_pose is None:
            return

        dx = self.target_x - self.current_pose.x
        dy = self.target_y - self.current_pose.y
        distance = math.sqrt(dx * dx + dy * dy)

        desired_heading = math.atan2(dy, dx)
        heading_error = desired_heading - self.current_pose.theta
        heading_error = math.atan2(math.sin(heading_error), math.cos(heading_error))

        command = Twist()
        if distance < 0.1:
            command.linear.x = 0.0
            command.angular.z = 0.0
            self.cmd_pub.publish(command)
            self.get_logger().info('Reached target position.')
            self.timer.cancel()
            return

        command.linear.x = min(2.0, 1.5 * distance)
        command.angular.z = 4.0 * heading_error
        self.cmd_pub.publish(command)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MoveToGoal()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
