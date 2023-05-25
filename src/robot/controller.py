import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan as LaserScanData
from cv_bridge import CvBridge
from modules.publishers import Velocity, Camera
from modules.subscribers import Position, EulerData, Lidar, Imu, ImuData
import cv2
import base64

class TurtleBotController(Node):
    __euler_data = EulerData()
    __lidar_data = LaserScanData()
    __imu_data = ImuData()

    __velocity_module = None
    __position_module = None
    __lidar_module = None
    __camera_module = None

    def __init__(self):
        super().__init__("turtlebot_controller")

        self.__velocity_module = Velocity(self)
        self.__position_module = Position(self, self.__position_callback)
        self.__lidar_module = Lidar(self, self.__lidar_callback)
        self.__imu_module = Imu(self, self.__imu_callback)
        self.__camera_module = Camera(self)
        self.video_capture = cv2.VideoCapture("src/robot/videoteste.mp4")

        self.create_timer(1, self.__runtime)

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

    def __runtime(self):
        
        
        while True:
            self.get_logger().info("Starting camera video")
            self.bridge = CvBridge()
            ret, frame = self.video_capture.read()
            if ret == True:
                self.__camera_module.apply(self.bridge.cv2_to_imgmsg(frame))
                print("oublicando")
            else:
                break
            
        
        # while True:
        #     ret, frame = video_capture.read()
        #     if not ret:  # Verifica se o frame é válido
        #         break  # Interrompe o loop se não há mais quadros
            
        #     self.__camera_module.apply(frame)
        # self.get_logger().info("End of camera video")

if __name__ == "__main__":
    rclpy.init()
    node = TurtleBotController()
    rclpy.spin(node)
    rclpy.shutdown()