from .base import Subscription
from rclpy.node import Node
from typing import Any
from sensor_msgs.msg import Image

class Streaming(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("streaming", node, "/camera", Image)

        super().connect(subscription_callback)