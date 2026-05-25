import select
import sys
import termios
import tty

import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node


class DriveNode(Node):
    """Keyboard teleoperation node publishing Twist messages on /cmd_vel."""

    def __init__(self):
        super().__init__("cosmo_rover_drive")
        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)

        self.linear_speed = 0.25
        self.angular_speed = 0.8
        self.speed_step = 0.05
        self.min_speed = 0.05
        self.max_speed = 1.0
        self.last_command = Twist()

        self.get_logger().info("Cosmo Rover keyboard drive ready")
        self.print_help()

    def print_help(self):
        print("")
        print("Cosmo Rover keyboard controls")
        print("-----------------------------")
        print("Up arrow    : forward")
        print("Down arrow  : backward")
        print("Left arrow  : turn left")
        print("Right arrow : turn right")
        print("q           : increase speed")
        print("a           : decrease speed")
        print("space       : stop")
        print("Ctrl+C      : quit")
        print("")

    def publish_command(self, linear_x=0.0, angular_z=0.0):
        message = Twist()
        message.linear.x = linear_x
        message.angular.z = angular_z
        self.last_command = message
        self.publisher.publish(message)

    def increase_speed(self):
        self.linear_speed = min(self.max_speed, self.linear_speed + self.speed_step)
        self.get_logger().info(f"Linear speed: {self.linear_speed:.2f} m/s")

    def decrease_speed(self):
        self.linear_speed = max(self.min_speed, self.linear_speed - self.speed_step)
        self.get_logger().info(f"Linear speed: {self.linear_speed:.2f} m/s")

    def handle_key(self, key):
        if key == "\x1b[A":
            self.publish_command(linear_x=self.linear_speed)
        elif key == "\x1b[B":
            self.publish_command(linear_x=-self.linear_speed)
        elif key == "\x1b[D":
            self.publish_command(angular_z=self.angular_speed)
        elif key == "\x1b[C":
            self.publish_command(angular_z=-self.angular_speed)
        elif key == "q":
            self.increase_speed()
        elif key == "a":
            self.decrease_speed()
        elif key == " ":
            self.publish_command()


def read_key():
    """Read one key press, including arrow escape sequences."""
    if not select.select([sys.stdin], [], [], 0.1)[0]:
        return None

    key = sys.stdin.read(1)
    if key == "\x1b" and select.select([sys.stdin], [], [], 0.01)[0]:
        key += sys.stdin.read(2)
    return key


def main(args=None):
    rclpy.init(args=args)
    node = DriveNode()
    terminal_settings = termios.tcgetattr(sys.stdin)

    try:
        tty.setcbreak(sys.stdin.fileno())

        while rclpy.ok():
            rclpy.spin_once(node, timeout_sec=0.0)
            key = read_key()

            if key is not None:
                node.handle_key(key)
    except KeyboardInterrupt:
        node.get_logger().info("Cosmo Rover drive node stopped")
    finally:
        node.publish_command()
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, terminal_settings)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
