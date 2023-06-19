from .base import Subscription
from rclpy.node import Node
from typing import Any
from std_msgs.msg import String

class GPS(Subscription):
    def __init__(self, node: Node, gps_callback: Any):
        super().__init__("gps", node, "/gps", String) 

        super().connect(gps_callback)