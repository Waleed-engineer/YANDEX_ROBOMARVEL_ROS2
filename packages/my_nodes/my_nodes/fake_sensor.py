import random 
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Float32, "/my_sensor", 10)
        self.timer = self.create_timer(0.2, self.send_message)

    def send_message(self):
        msg = Float32()
        msg.data = random.uniform(22.0, 28.0)
        self.pub.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data:.2f}')


def main():
    rclpy.init()
    node = Talker()
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
