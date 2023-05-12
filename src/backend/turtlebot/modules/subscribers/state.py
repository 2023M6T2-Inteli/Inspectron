from .base import Subscription
from rclpy.node import Node
from typing import Any

class State(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("state", node, "state")
        super().connect(subscription_callback)
        