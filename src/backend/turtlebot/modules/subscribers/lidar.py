from .base import Subscription
from rclpy.node import Node
from typing import Any

class Lidar(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("lidar", node, "lidar")
        super().connect(subscription_callback)
        