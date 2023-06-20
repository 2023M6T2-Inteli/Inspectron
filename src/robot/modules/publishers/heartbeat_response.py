from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import String
import json


class HeartbeatResponse(Publisher):
    def __init__(self, node: Node):
        super().__init__("heartbeat_response", node, f"/heartbeat_response", String)

    def pong(self):
        response = {
            "status": "ALIVE",
        }
        self.publish(String(data=json.dumps(response)))
