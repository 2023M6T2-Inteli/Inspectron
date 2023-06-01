from .base import Publisher
from rclpy.node import Node
import json

from std_msgs.msg import String

class BackendCommands(Publisher):
    def __init__(self, node: Node):
        super().__init__("BackendCommands", node, f"/backend_commands", String)

    def send(self, msg):
        message = String()
        message.data = json.dumps(msg)

        self.publish(message=message)
