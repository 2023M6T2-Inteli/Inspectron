from .base import Publisher
from rclpy.node import Node

from std_msgs.msg import String

class Heartbeat(Publisher):
    def __init__(self, node: Node):
        super().__init__("Heartbeat", node, f"/heartbeat", String)

    def send(self, msg):
        message = String()
        message.data = msg

        self.publish(message)
        print("Mensagem publicada com sucesso!", flush=True)
