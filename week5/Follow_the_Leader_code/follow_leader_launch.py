import time
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction


def generate_launch_description():
    return LaunchDescription([
        # 1. Start the turtlesim simulator (spawns turtle1 by default)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen',
        ),

        # 2. Keyboard teleop for turtle1 (opens in a new xterm window)
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -title "Teleop turtle1 — use arrow keys" -e',
            output='screen',
        ),

        # 3. Spawn turtle2 after a short delay so turtlesim is ready
        TimerAction(
            period=1.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'service', 'call', '/spawn',
                        'turtlesim/srv/Spawn',
                        '{x: 2.0, y: 2.0, theta: 0.0, name: "turtle2"}'
                    ],
                    output='screen',
                ),
            ]
        ),

        # 4. Start the follow-leader node after turtle2 is spawned
        TimerAction(
            period=2.0,
            actions=[
                Node(
                    package='my_launch_pkg',
                    executable='follow_leader',
                    name='follow_leader',
                    output='screen',
                ),
            ]
        ),
    ])
