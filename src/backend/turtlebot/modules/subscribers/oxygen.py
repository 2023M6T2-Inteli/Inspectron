from .base import Subscription
from rclpy.node import Node
from typing import Any

class Oxygen(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("oxigen", node, "oxigen")
        super().connect(subscription_callback)
        