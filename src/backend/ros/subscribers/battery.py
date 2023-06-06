from .base import Subscription
from rclpy.node import Node
from typing import Any
from sensor_msgs.msg import BatteryState

class Battery(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("battery", node, "/battery_state", BatteryState) 

        super().connect(subscription_callback)