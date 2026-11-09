import rclpy
from rclpy.node import Node


class HelloNode(Node):
    def __init__(self):
        super().__init__("countdown")
        self.ticks = 5
        self.timer = self.create_timer(1.0, self.on_timer)
        self.get_logger().info("Node countdown is running, waiting timer")

    def on_timer(self):
        if self.ticks > 1:
            self.get_logger().info(f" Tick counter {self.ticks}")
            self.ticks -= 1
        elif self.ticks == 1:
            self.get_logger().info(f"LETS GO!")
            self.ticks -= 1
            self.timer.cancel()

def main():
    rclpy.init()
    node = HelloNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
