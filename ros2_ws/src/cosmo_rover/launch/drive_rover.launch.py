from os.path import join

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():
    """Launch Gazebo with the simple Cosmo Rover world."""
    package_share_dir = get_package_share_directory("cosmo_rover")
    world_path = join(package_share_dir, "worlds", "simple_track.sdf")

    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gz", "sim", world_path],
                output="screen",
            )
        ]
    )
