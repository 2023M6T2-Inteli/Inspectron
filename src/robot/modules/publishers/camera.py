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
<<<<<<< HEAD
        total_frames = int(self.__video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        print("Total frames in the video: %d" % total_frames)
        frame_rate = self.__video_capture.get(5)
        duration = total_frames / frame_rate
=======
        returned, frame = self.__video_capture.read()
        if not returned:
            return
>>>>>>> d6b8285bf7d893ac7c0d6315367427f4f66113f5

        self.publish(self.__bridge.cv2_to_imgmsg(frame, encoding="bgr8"))
