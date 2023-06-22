from .base import Subscription
from rclpy.node import Node
from typing import Any
from sensor_msgs.msg import LaserScan
from enum import Enum
from rclpy.qos import qos_profile_sensor_data
import rclpy
import numpy as np
import math


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
    def find_nearest_index(data: list, angle: float) -> int:
        angle %= 2 * np.pi
        angle_indices = np.linspace(0, 2 * np.pi, len(data), endpoint=False)
        nearest_index = np.argmin(np.abs(angle_indices - angle))
        return nearest_index

    @staticmethod
    def remap_to_scan(data: list) -> list:
        angles = np.linspace(0, 2 * np.pi, len(data.ranges), endpoint=False)
        remapped_ranges = np.interp(np.linspace(0, 2 * np.pi, 360, endpoint=False), angles, data.ranges)
        return remapped_ranges.tolist()

    @staticmethod
    def get_distance(lidar_data: LaserScan, angles: list, distance_type: DistanceFilterType) -> float:
        valid_ranges = []
        for i in angles:
            if i >= 0 and i < len(lidar_data.ranges):
                range_value = lidar_data.ranges[i]
                if not math.isnan(range_value):
                    valid_ranges.append(range_value)

        if len(valid_ranges) == 0:
            return float("nan")

        return round(DistanceFilterFunctions.MAP[distance_type](valid_ranges), 3)

    def frontal_distance(self, distance_type: DistanceFilterType) -> float:
        return self.get_distance(self.__data, range(-30, 30), distance_type)

    def right_distance(self, distance_type: DistanceFilterType) -> float:
        return self.get_distance(self.__data, range(240, 300), distance_type)

    def left_distance(self, distance_type: DistanceFilterType) -> float:
        return self.get_distance(self.__data, range(60, 120), distance_type)

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
