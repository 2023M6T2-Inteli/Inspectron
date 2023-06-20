from .base import Publisher
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class Camera(Publisher):
    def __init__(self, node: Node):
        super().__init__("camera", node, f"/camera", Image)
        self.__video_capture = cv2.VideoCapture(0)
        self.__video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.__video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.__bridge = CvBridge()

    def update(self):
        returned, frame = self.__video_capture.read()
        if not returned:
            return

        self.publish(self.__bridge.cv2_to_imgmsg(frame, encoding="bgr8"))
