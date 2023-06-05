from .base import Subscription
from rclpy.node import Node
from typing import Any
from std_msgs.msg import String

class Heartbeat(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("Heartbeat", node, f"/heartbeat", String)

        super().connect(lambda msg: subscription_callback(msg))

    