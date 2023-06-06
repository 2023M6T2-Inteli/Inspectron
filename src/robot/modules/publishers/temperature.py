from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import Float64

class Temperature(Publisher):
    def __init__(self, node: Node):
        super().__init__("Temperature", node, f"/temperature", Float64)

    def send(self, msg):
        self.publish(Float64(data=float(msg)))

    