from .base import Subscription
from rclpy.node import Node
from typing import Any
from std_msgs.msg import String

class BackendCommands(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("BackendCommands", node, f"/backend_commands", String)

        super().connect(lambda msg: subscription_callback(msg))

    