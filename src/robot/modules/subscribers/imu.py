from .base import Subscription
from rclpy.node import Node
from typing import Any
from sensor_msgs.msg import Imu as ImuMsgData


class ImuDataVector3:
    x = None
    y = None
    z = None

    def __init__(self, x: float = None, y: float = None, z: float = None):
        self.x = round(x, 3)
        self.y = round(y, 3)
        self.z = round(z, 3)

    def __repr__(self):
        return f"ImuDataVector3({self.x}, {self.y}, {self.z})"

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


class ImuData:
    orientation = None
    angular_velocity = None
    linear_acceleration = None

    def __init__(self, orientation: ImuDataVector3 = None, angular_velocity: ImuDataVector3 = None, linear_acceleration: ImuDataVector3 = None):
        self.orientation = orientation
        self.angular_velocity = angular_velocity
        self.linear_acceleration = linear_acceleration

    def __repr__(self):
        return f"ImuData({self.orientation}, {self.angular_velocity}, {self.linear_acceleration})"

    def __str__(self):
        return f'({self.orientation}, {self.angular_velocity}, {self.linear_acceleration})'


class Imu(Subscription):
    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("Lidar", node, f"/imu", ImuMsgData)

        super().connect(lambda msg: subscription_callback(self.__parse_middleware(msg)))

    def __parse_middleware(self, data: ImuMsgData) -> ImuData:
        orientation = ImuDataVector3(data.orientation.x, data.orientation.y, data.orientation.z)
        angular_velocity = ImuDataVector3(data.angular_velocity.x, data.angular_velocity.y, data.angular_velocity.z)
        linear_acceleration = ImuDataVector3(data.linear_acceleration.x, data.linear_acceleration.y, data.linear_acceleration.z)

        return ImuData(orientation, angular_velocity, linear_acceleration)
