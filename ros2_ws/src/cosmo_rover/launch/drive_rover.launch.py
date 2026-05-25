import os
from os.path import join

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable


def generate_launch_description():
    """Launch Gazebo with the simple Cosmo Rover world."""
    package_share_dir = get_package_share_directory("cosmo_rover")
    world_path = join(package_share_dir, "worlds", "simple_track.sdf")
    model_path = join(package_share_dir, "models")
    existing_resource_path = os.environ.get("GZ_SIM_RESOURCE_PATH", "")
    resource_path = (
        model_path
        if not existing_resource_path
        else model_path + os.pathsep + existing_resource_path
    )

    return LaunchDescription(
        [
            SetEnvironmentVariable("GZ_SIM_RESOURCE_PATH", resource_path),
            ExecuteProcess(
                cmd=["gz", "sim", world_path],
                output="screen",
            )
        ]
    )
