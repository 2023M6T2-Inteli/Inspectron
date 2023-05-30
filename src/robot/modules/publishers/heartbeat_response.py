from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import String


class HeartbeatResponse(Publisher):
    def __init__(self, node: Node):
        super().__init__("heartbeat_response", node, f"/heartbeat_response", String)

    def apply(self, msg: String):
        self.publish(String(data=str(msg)))