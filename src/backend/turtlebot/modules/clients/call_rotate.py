from .base import Client
from rclpy.node import Node

class CallRotate(Client):
    def __init__(self, node: Node):
        super().__init__("call_rotate", node, "call_rotate", Rotate)
        
    def execute(self, degrees, speed):
        self.async_call(Rotate(degrees, speed))
