from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import String

class Camera(Publisher):
    def __init__(self, node: Node):
        super().__init__("camera", node, f"/camera", String)

    def send(self, converted_string):
        msg = String(data=converted_string)
        self.publish(msg)