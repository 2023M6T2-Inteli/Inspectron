from .base import Publisher
from rclpy.node import Node

from std_msgs.msg import String

class BackendCommands(Publisher):
    def __init__(self, node: Node):
        super().__init__("BackendCommands", node, f"/backend_commands", String)

    def send(self, msg):
        self.publish(msg)
