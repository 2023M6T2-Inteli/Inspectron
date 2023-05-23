from .base import Subscription
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from typing import Any

class Streaming(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("streaming", node, f"/streaming", Odometry)

        super().connect(subscription_callback)