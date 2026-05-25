from setuptools import find_packages, setup

package_name = "cosmo_rover"

setup(
    name=package_name,
    version="0.0.1",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        ("share/" + package_name + "/launch", ["launch/rover_timer.launch.py"]),
        ("share/" + package_name + "/worlds", ["worlds/simple_track.sdf"]),
        (
            "share/" + package_name + "/models/cosmo_rover",
            ["models/cosmo_rover/model.config", "models/cosmo_rover/model.sdf"],
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Laurent Moreschi",
    maintainer_email="laurent@example.com",
    description="Simple ROS 2 starter package for the Cosmo Rover timer workflow.",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "timer_node = cosmo_rover.timer_node:main",
        ],
    },
)
