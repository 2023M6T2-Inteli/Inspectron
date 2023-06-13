from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import Float64
from sensors import EnvironmentSensor


class TVOC(Publisher):
    def __init__(self, node: Node):
        super().__init__("TVOC", node, f"/tvoc", Float64)

    def update(self):
        tvoc = EnvironmentSensor.get_tvoc()
        if tvoc:
            self.publish(Float64(data=float(tvoc)))
