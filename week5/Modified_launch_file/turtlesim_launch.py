from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess


def generate_launch_description():
    return LaunchDescription([
        # Launch the turtlesim node (this gives us turtle1 by default)
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        # Launch keyboard teleop for turtle1
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e',
            remappings=[
                ('/turtle1/cmd_vel', '/turtle1/cmd_vel'),
            ]
        ),

        # Spawn a second turtle using the turtlesim /spawn service
        ExecuteProcess(
            cmd=[
                'ros2', 'service', 'call', '/spawn',
                'turtlesim/srv/Spawn',
                '{x: 2.0, y: 2.0, theta: 0.0, name: "turtle2"}'
            ],
            output='screen'
        ),
    ])
