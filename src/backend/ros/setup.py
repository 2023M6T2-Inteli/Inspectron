import rclpy
from rclpy.node import Node
from ultralytics import YOLO
import cv2
from cv_bridge import CvBridge
from ros.subscribers import Camera, HeartbeatResponse
from ros.publisher import BackendCommands, Heartbeat
import json
import websockets
import base64
import asyncio
class BackendController(Node):
    def __init__(self, sio):
        super().__init__("backend_controller")
        self.sio = sio
        self.camera_module = Camera(self, self.__camera_callback)
        self.heartbeat_response_module = HeartbeatResponse(self, self.__heartbeat_response_callback)
        self.heartbeat = Heartbeat(self)
        self.bridge = CvBridge()
        self.backend_commands = BackendCommands(self)
        

    def __camera_callback(self, data):
        self.get_logger().info('Receiving video frame')
        
        current_frame = self.bridge.imgmsg_to_cv2(data)
        model = YOLO(".yolo.pt")
        result = model.predict(current_frame, conf=0.6)
        annotated = result[0].plot()
        _, frame = cv2.imencode(".jpg", annotated)
        frame64 = base64.b64encode(frame).decode("utf-8")
        print(frame64)
        self.sio.emit("camera", frame64)
        

    def __heartbeat_response_callback(self, data):
        self.backend_commands.send({'command': 'START', 'body': ''})

        # self.sio.emit("streaming", converted_string)
        # self.get_logger().info(f"Received message: {msg}")
      
        
# def main(args=None):
#     rclpy.init(args=args)
#     image_subscriber = BackendController()
#     rclpy.spin(image_subscriber)
#     image_subscriber.destroy_node()
#     rclpy.shutdown()
  
# if __name__ == '__main__':
#   main()
        
        
        
        
        
        
      