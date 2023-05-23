import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan

from modules.publishers import Velocity
from modules.subscribers import Position, EulerData, Lidar

class TurtleBotController(Node):
    __euler_data = EulerData()
    __lidar_data = LaserScan()

    def __init__(self):
        super().__init__("turtlebot_controller")

        self.velocity_module = Velocity(self)
        self.position_module = Position(self, self.__position_callback)
        self.lidar_module = Lidar(self, self.__lidar_callback)

        self.create_timer(1, self.__publish_velocity)

    def __position_callback(self, euler_data: EulerData):
        self.__euler_data = euler_data
        #self.get_logger().info(str(euler_data))

    def __lidar_callback(self, lidar_data: LaserScan):
		# lidar_data.ranges = array of 360 values (0-360 degrees) of distance in meters
        self.__lidar_data = lidar_data
        self.get_logger().info(str(lidar_data.ranges))

    def __publish_velocity(self):
        self.velocity_module.apply(Vector3(x=0.0, y=0.0, z=0.0), Vector3(x=0.0, y=0.0, z=0.0))

if __name__ == "__main__":
    rclpy.init()
    node = TurtleBotController()
    rclpy.spin(node)
    rclpy.shutdown()