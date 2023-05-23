import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan as LaserScanData

from modules.publishers import Velocity
from modules.subscribers import Position, EulerData, Lidar, Imu, ImuData

class TurtleBotController(Node):
    __euler_data = EulerData()
    __lidar_data = LaserScanData()
    __imu_data = ImuData()

    __velocity_module = None
    __position_module = None
    __lidar_module = None

    def __init__(self):
        super().__init__("turtlebot_controller")

        self.__velocity_module = Velocity(self)
        self.__position_module = Position(self, self.__position_callback)
        self.__lidar_module = Lidar(self, self.__lidar_callback)
        self.__imu_module = Imu(self, self.__imu_callback)

        self.create_timer(1, self.__publish_velocity)



    def __position_callback(self, euler_data: EulerData):
        self.__euler_data = euler_data
        #self.get_logger().info(str(euler_data))

    def __lidar_callback(self, lidar_data: LaserScanData):
        # lidar_data.ranges = array of 360 values (0-360 degrees) of distance in meters
        self.__lidar_data = lidar_data
        #self.get_logger().info(str(lidar_data.ranges))

    def __imu_callback(self, imu_data: ImuData):
        self.__imu_data = imu_data
        #self.get_logger().info(str(imu_data))

    def __publish_velocity(self):
        self.__velocity_module.apply(1, 0)

if __name__ == "__main__":
    rclpy.init()
    node = TurtleBotController()
    rclpy.spin(node)
    rclpy.shutdown()