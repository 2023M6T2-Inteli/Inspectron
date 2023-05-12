from .base import Subscription
from rclpy.node import Node
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from typing import Any

class EulerData:
    x: float
    y: float
    z: float
    roll: float
    pitch: float
    yaw: float

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.roll = 0.0
        self.pitch = 0.0
        self.yaw = 0.0

    def from_dict(self, data: dict):
        self.x = round(data["x"], 3)
        self.y = round(data["y"], 3)
        self.z = round(data["z"], 3)
        self.roll = round(data["roll"], 3)
        self.pitch = round(data["pitch"], 3)
        self.yaw = round(data["yaw"], 3)

        return self

    def __repr__(self):
        return f"EulerData(x={self.x}, y={self.y}, z={self.z}, roll={self.roll}, pitch={self.pitch}, yaw={self.yaw})"

    def __str__(self):
        return self.__repr__()

class Position(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("pose", node, f"/odom", Odometry)

        super().connect(lambda msg: subscription_callback(self.__parse_middleware(msg)))

    def __parse_middleware(self, msg: Odometry):
            orientation = msg.pose.pose.orientation
            orientation = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
            return EulerData().from_dict({
                "x": msg.pose.pose.position.x,
                "y": msg.pose.pose.position.y,
                "z": msg.pose.pose.position.z,
                "roll": orientation[0],
                "pitch": orientation[1],
                "yaw": orientation[2]
            })
