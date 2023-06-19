from .base import Publisher
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class Camera(Publisher):
    def __init__(self, node: Node):
        super().__init__("camera", node, f"/camera", Image)
        self.__video_capture = cv2.VideoCapture(0, cv2.CAP_PROP_FRAME_WIDTH, 320, cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.__bridge = CvBridge()

    def update(self):
        total_frames = int(self.__video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        print("Total frames in the video: %d" % total_frames)
        frame_rate = self.__video_capture.get(cv2.CAP_PROP_FPS)
        duration = total_frames / frame_rate

        print("Duration to show %d frames: %.2f seconds" % (total_frames, duration))
        # Read video and publish frames

        while True:
            returned, frame = self.__video_capture.read()
            if not returned:
                break

            self.publish(self.__bridge.cv2_to_imgmsg(frame, encoding="bgr8"))
