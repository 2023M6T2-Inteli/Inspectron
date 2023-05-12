from .base import Subscription
from rclpy.node import Node
from typing import Any

class Imu(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("imu", node, "imu")
        super().connect(subscription_callback)
        