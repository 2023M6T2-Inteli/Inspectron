from .base import Subscription
from rclpy.node import Node
from typing import Any
from sensor_msgs.msg import LaserScan
from enum import Enum
from rclpy.qos import qos_profile_sensor_data
import rclpy
from numpy import interp


class DistanceFilterType(Enum):
    AVERAGE = 1
    MIN = 2
    MAX = 3


class DistanceFilterFunctions:
    MAP = {
        DistanceFilterType.AVERAGE: lambda data: sum(data) / len(data),
        DistanceFilterType.MIN: lambda data: min(data),
        DistanceFilterType.MAX: lambda data: max(data)
    }


class Lidar(Subscription):
    __data = LaserScan()

    def __init__(self, node: Node, subscription_callback: Any):
        super().__init__("Lidar", node, f"/scan", LaserScan, qos_profile_sensor_data)
        super().connect(lambda data: subscription_callback(self.__middleware(data)))

    def __middleware(self, lidar_data: LaserScan) -> LaserScan:
        lidar_data.ranges = self.remap_to_scan(lidar_data)
        self.__data = lidar_data
        return lidar_data

    @staticmethod
    def find_nearest_index(data: list, index: float) -> int:
        return min(range(len(data)), key=lambda i: abs(data[i] - index))

    @staticmethod
    def remap_to_scan(data: list) -> list:
        # print(len(data.ranges))
        # print(data.ranges)
        new_list = []

        for i in range(360):
            index = interp(i, [0, 360], [0, len(data.ranges)])
            new_list.append(
                data.ranges[Lidar.find_nearest_index(data.ranges, index)])
        return new_list

    @staticmethod
    def get_distance(lidar_data: LaserScan, angles: list, distance_type: DistanceFilterType) -> float:
        if len(angles) == 0 or len(lidar_data.ranges) == 0:
            return float("inf")

        return round(DistanceFilterFunctions.MAP[distance_type]([lidar_data.ranges[i] for i in angles]), 3)

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
