import rclpy
from rclpy.node import Node

from ultralytics import YOLO
import cv2
import base64

from ros.subscribers import Streaming


class BackendController(Node):
    def __init__(self, sio):
        super().__init__("backend_controller")
        self.sio = sio
        self.streaming_module = Streaming(self, self.__streaming_callback)
        
    def __streaming_callback(self, msg):
        
        #Converte de base64 para imagem
        decoded_data=base64.b64decode(msg)
        
        #Passa pelo modelo preditivo
        model = YOLO("./yolo.pt")
        result = model.predict(decoded_data, conf=0.4)
        annotated_frame = result[0].plot()

        #Converte novamente para base64
        converted_string = base64.b64encode(annotated_frame) 

        self.sio.emit("streaming", converted_string)
        self.get_logger().info(f"Received message: {msg}")