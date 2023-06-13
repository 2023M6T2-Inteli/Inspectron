from .base import Publisher
from rclpy.node import Node
from std_msgs.msg import Float64
from sensors import EnvironmentSensor


class ECO2(Publisher):
    def __init__(self, node: Node):
        super().__init__("ECO2", node, f"/eco2", Float64)

    def update(self):
        eco2 = EnvironmentSensor.get_eco2()
        if eco2:
            self.publish(Float64(data=float(eco2)))
