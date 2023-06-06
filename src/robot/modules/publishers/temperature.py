from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import Float64
from sensors import DHT11


class Temperature(Publisher):
    def __init__(self, node: Node):
        super().__init__("Temperature", node, f"/temperature", Float64)

    def update(self):
        self.publish(Float64(data=float(DHT11.get_temperature())))
