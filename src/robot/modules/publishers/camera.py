from .base import Publisher
from rclpy.node import Node
import cv2
import base64
from std_msgs.msg import String

class Camera(Publisher):
    def __init__(self, node: Node):
        super().__init__("camera", node, f"/camera", String) 

    def apply(self):
        video_capture = cv2.VideoCapture(0)
        _, frame = video_capture.read()
        converted_string = base64.b64encode(frame) 
        self.publish(converted_string)