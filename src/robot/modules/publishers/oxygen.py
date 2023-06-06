from .base import Publisher
from rclpy.node import Node
from typing import Any
from std_msgs.msg import Float64


class Oxygen(Publisher):
    def __init__(self, node: Node):
        super().__init__("Oxygen", node, f"/oxygen", Float64)

    def send(self, msg):
        self.publish(Float64(data=float(msg)))
