import rclpy
from rclpy.node import Node

from subscribers import Streaming

class BackendController(Node):
    def __init__(self, sio):
        super().__init__("backend_controller")
        self.sio = sio
        self.streaming_module = Streaming(self, self.__streaming_callback)
        
    def __streaming_callback(self, msg):
        

        self.sio.emit("streaming", msg)
        self.get_logger().info(f"Received message: {msg}")