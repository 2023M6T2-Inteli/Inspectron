from .base import Subscription
from rclpy.node import Node
from typing import Any
from sensor_msgs.msg import LaserScan
from enum import Enum

class DistanceFilterType(Enum):
    AVERAGE = 1
    MIN = 2
    MAX = 3


class Lidar(Subscription):
    __data = LaserScan()

    def __init__(self, node: Node, subscription_callback: Any):
        # lidar_data.ranges = array of 360 values (0-360 degrees) of distance in meters
        super().__init__("Lidar", node, f"/scan", LaserScan)
        super().connect(lambda data: subscription_callback(self.__middleware(data)))

    def __middleware(self, lidar_data: LaserScan) -> LaserScan:
        self.__data = lidar_data
        return lidar_data

    @staticmethod
    def get_distance(lidar_data: LaserScan, angles: list, distance_type: DistanceFilterType) -> float:
        if len(angles) == 0 or len(lidar_data.ranges) == 0:
            return float("inf")

        if distance_type == DistanceFilterType.AVERAGE:
            return sum([lidar_data.ranges[angle] for angle in angles]) / len(angles)
        elif distance_type == DistanceFilterType.MIN:
            return min([lidar_data.ranges[angle] for angle in angles])
        elif distance_type == DistanceFilterType.MAX:
            return max([lidar_data.ranges[angle] for angle in angles])

    def frontal_distance(self, distance_type: DistanceFilterType) -> float:
        return self.get_distance(self.__data, range(-30, 30), distance_type)

    def right_distance(self, distance_type: DistanceFilterType) -> float:
        return self.get_distance(self.__data, range(60, 120), distance_type)

    def left_distance(self, distance_type: DistanceFilterType) -> float:
        return self.get_distance(self.__data, range(240, 300), distance_type)

    def back_distance(self, distance_type: DistanceFilterType) -> float:
        return self.get_distance(self.__data, range(150, 210), distance_type)

    @property
    def min_distances(self) -> list:
        return (self.frontal_distance(DistanceFilterType.MIN), self.right_distance(DistanceFilterType.MIN), self.left_distance(DistanceFilterType.MIN), self.back_distance(DistanceFilterType.MIN))

    @property
    def max_distances(self) -> list:
        return (self.frontal_distance(DistanceFilterType.MAX), self.right_distance(DistanceFilterType.MAX), self.left_distance(DistanceFilterType.MAX), self.back_distance(DistanceFilterType.MAX))

    @property
    def average_distances(self) -> list:
        return (self.frontal_distance(DistanceFilterType.AVERAGE), self.right_distance(DistanceFilterType.AVERAGE), self.left_distance(DistanceFilterType.AVERAGE), self.back_distance(DistanceFilterType.AVERAGE))