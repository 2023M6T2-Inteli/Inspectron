from .base import Subscription
from rclpy.node import Node
from typing import Any
#from sensor_msgs.msg import BatteryState

class Oxygen(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("oxygen", node, "/oxygen") 

        super().connect(subscription_callback)