from .base import Publisher
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class Camera(Publisher):
    def __init__(self, node: Node):
        super().__init__("camera", node, f"/camera", Image)


    def send(self, img):
        print("Imagem enviada com sucesso!")
        self.publish(img)

