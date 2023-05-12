from .base import Subscription
from rclpy.node import Node
from typing import Any

class CameraStream(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("camera_stream", node, "camera_stream")
        super().connect(subscription_callback)
        