#!/usr/bin/env python3

import math

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class MoveTurtlePattern(Node):
    def __init__(self) -> None:
        super().__init__('move_turtle_pattern')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.declare_parameter('pattern', 'circle')
        self.pattern = self.get_parameter('pattern').get_parameter_value().string_value

        if self.pattern == 'triangle':
            self.phase = 0
            self.phase_ticks = 0
            self.timer = self.create_timer(0.1, self._triangle_step)
        else:
            self.timer = self.create_timer(0.1, self._circle_step)

        self.get_logger().info(f'Running pattern: {self.pattern}')

    def _publish(self, linear_x: float, angular_z: float) -> None:
        message = Twist()
        message.linear.x = linear_x
        message.angular.z = angular_z
        self.publisher.publish(message)

    def _circle_step(self) -> None:
        self._publish(2.0, 1.0)

    def _triangle_step(self) -> None:
        move_ticks = 20
        turn_ticks = 8

        if self.phase % 2 == 0:
            if self.phase_ticks < move_ticks:
                self._publish(2.0, 0.0)
            else:
                self.phase += 1
                self.phase_ticks = -1
        else:
            if self.phase_ticks < turn_ticks:
                self._publish(0.0, (math.pi / 3.0) / (turn_ticks * 0.1))
            else:
                self.phase += 1
                self.phase_ticks = -1

        self.phase_ticks += 1


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MoveTurtlePattern()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
