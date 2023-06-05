from .base import Subscription
from rclpy.node import Node
from typing import Any
from std_msgs.msg import String

class HeartbeatResponse(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("heartbeat_response", node, "/heartbeat_response", String)

        super().connect(subscription_callback)