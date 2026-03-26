#!/usr/bin/env python3

import math
from typing import Dict

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node
from rclpy.publisher import Publisher
from turtlesim.srv import Spawn


class MultiTurtlePatterns(Node):
    def __init__(self) -> None:
        super().__init__('multi_turtle_patterns')
        self.spawn_client = self.create_client(Spawn, '/spawn')
        self.cmd_publishers: Dict[str, Publisher] = {}
        self.tick = 0

        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')

        self._spawn_turtle(2.0, 2.0, 0.0, 'turtle2')
        self._spawn_turtle(8.0, 2.0, 0.0, 'turtle3')
        self._spawn_turtle(5.0, 8.0, 0.0, 'turtle4')

        for name in ('turtle1', 'turtle2', 'turtle3', 'turtle4'):
            self.cmd_publishers[name] = self.create_publisher(Twist, f'/{name}/cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('Spawned turtles and started patterns.')

    def _spawn_turtle(self, x: float, y: float, theta: float, name: str) -> None:
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name

        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is None:
            self.get_logger().warning(f'Could not spawn {name}; it may already exist.')

    def _publish(self, turtle_name: str, linear_x: float, angular_z: float) -> None:
        message = Twist()
        message.linear.x = linear_x
        message.angular.z = angular_z
        self.cmd_publishers[turtle_name].publish(message)

    def timer_callback(self) -> None:
        self._publish('turtle1', 2.0, 1.0)

        step = self.tick % 56
        if step < 20:
            self._publish('turtle2', 2.0, 0.0)
        elif step < 28:
            self._publish('turtle2', 0.0, (math.pi / 2.0) / (8 * 0.1))
        elif step < 48:
            self._publish('turtle2', 2.0, 0.0)
        else:
            self._publish('turtle2', 0.0, (math.pi / 2.0) / (8 * 0.1))

        step3 = self.tick % 96
        if step3 < 24:
            self._publish('turtle3', 2.0, 0.0)
        elif step3 < 32:
            self._publish('turtle3', 0.0, (2 * math.pi / 3.0) / (8 * 0.1))
        elif step3 < 56:
            self._publish('turtle3', 2.0, 0.0)
        elif step3 < 64:
            self._publish('turtle3', 0.0, (2 * math.pi / 3.0) / (8 * 0.1))
        elif step3 < 88:
            self._publish('turtle3', 2.0, 0.0)
        else:
            self._publish('turtle3', 0.0, (2 * math.pi / 3.0) / (8 * 0.1))

        angle_rate = (2 * math.pi) / 8.0
        self._publish('turtle4', 1.5, angle_rate)

        self.tick += 1


def main(args=None) -> None:
    rclpy.init(args=args)
    node = MultiTurtlePatterns()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
