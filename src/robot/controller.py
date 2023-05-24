import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3

from modules.publishers import Velocity, Camera
from modules.subscribers import Position, EulerData
import cv2
import base64

class TurtleBotController(Node):
    __euler_data = EulerData()

    def __init__(self):
        super().__init__("turtlebot_controller")

        self.velocity_module = Velocity(self)
        self.position_module = Position(self, self.__position_callback)
        self.camera = Camera(self)

        self.create_timer(1, self.publish_velocity)

    def __position_callback(self, euler_data: EulerData):
        self.__euler_data = euler_data
        self.get_logger().info(str(euler_data))

    def publish_velocity(self):
        self.get_logger().info("Publsoh realizado")
        
        self.velocity_module.apply(Vector3(x=0.0, y=0.0, z=0.0), Vector3(x=0.0, y=0.0, z=0.0))
        #self.camera.apply("oi")
        
        video_capture = cv2.VideoCapture("./videoteste.mp4")
        while True:
            _, frame = video_capture.read()
            converted_string = base64.b64encode(frame) 
            self.camera.apply(str(converted_string))

if __name__ == "__main__":
    rclpy.init()
    node = TurtleBotController()
    rclpy.spin(node)
    rclpy.shutdown()