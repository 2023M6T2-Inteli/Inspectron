from .base import Publisher
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class Camera(Publisher):
    def __init__(self, node: Node):
        super().__init__("camera", node, f"/camera", Image)
        self.__video_capture = cv2.VideoCapture(0)
        self.__bridge = CvBridge()

    def update(self):
        returned, frame = self.__video_capture.read()
        if returned:
            self.publish(self.__bridge.cv2_to_imgmsg(frame, encoding="bgr8"))
