from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import String
from sensors import GPSSensor
import json


class GPS(Publisher):
    def __init__(self, node: Node):
        super().__init__("GPS", node, f"/gps", String)

    def update(self):
        gps_data = GPSSensor.read_gps_data()
        if gps_data:
            self.publish(String(data=json.dumps(gps_data.to_dict())))
