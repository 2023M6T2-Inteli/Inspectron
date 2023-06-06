from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import Float64
from sensors import DHT11


class Humidity(Publisher):
    def __init__(self, node: Node):
        super().__init__("Humidity", node, f"/humidity", Float64)

    def update(self):
        self.publish(Float64(data=float(DHT11.get_humidity())))
