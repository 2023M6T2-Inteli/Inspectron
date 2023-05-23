from .base import Client
from rclpy.node import Node

class CallMove(Client):
    def __init__(self, node: Node):
        super().__init__("call_move", node, "call_move", Movement)
        
    def execute(self, motorA, motorB):
        self.async_call(Movement(motorA, motorB))
