from .base import Subscription
from rclpy.node import Node
from typing import Any
from std_msgs.msg import Float64

class Humidity(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("Humidity", node, "/humidity", Float64) 

        super().connect(subscription_callback)