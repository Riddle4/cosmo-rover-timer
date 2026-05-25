import rclpy
from rclpy.node import Node


class CosmoRoverTimer(Node):
    """ROS 2 node that prints elapsed time once per second."""

    def __init__(self):
        super().__init__("cosmo_rover_timer")
        self.elapsed_seconds = 0

        self.get_logger().info("Cosmo Rover Timer started")

        # The timer callback runs every second while rclpy spins this node.
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        self.elapsed_seconds += 1
        self.get_logger().info(f"Elapsed time: {self.elapsed_seconds} seconds")


def main(args=None):
    rclpy.init(args=args)
    node = CosmoRoverTimer()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Cosmo Rover Timer stopped")
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
