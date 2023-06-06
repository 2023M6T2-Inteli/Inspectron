from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import Float64


class Humidity(Publisher):
    def __init__(self, node: Node):
        super().__init__("Humidity", node, f"/humidity", Float64)

    def send(self, msg):
        self.publish(Float64(data=float(msg)))
