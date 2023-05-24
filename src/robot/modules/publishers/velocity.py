from .base import Publisher
from rclpy.node import Node
from geometry_msgs.msg import Twist, Vector3


class Velocity(Publisher):
    def __init__(self, node: Node):
        super().__init__("velocity", node, f"/cmd_vel", Twist)

    def apply(self, force_x: int, force_y: int) -> None:
        self.publish(Twist(linear=Vector3(x=float(force_x), y=0.0, z=0.0), angular=Vector3(x=0.0, y=0.0, z=float(force_y))))