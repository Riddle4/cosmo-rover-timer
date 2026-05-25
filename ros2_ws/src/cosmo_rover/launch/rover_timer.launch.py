from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    """Launch the simple Cosmo Rover timer node."""
    return LaunchDescription(
        [
            Node(
                package="cosmo_rover",
                executable="timer_node",
                name="cosmo_rover_timer",
                output="screen",
            )
        ]
    )
