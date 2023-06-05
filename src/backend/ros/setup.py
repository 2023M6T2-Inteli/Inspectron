import rclpy
from rclpy.node import Node
from ultralytics import YOLO
import cv2
from cv_bridge import CvBridge
from ros.subscribers import Streaming, HeartbeatResponse, Battery, Oxygen
from ros.publisher import BackendCommands, Heartbeat
import json

class BackendController(Node):
    def __init__(self, sio):
        super().__init__("backend_controller")
        self.sio = sio
        self.streaming_module = Streaming(self, self.__streaming_callback)
        self.heartbeat_response_module = HeartbeatResponse(self, self.__heartbeat_response_callback)
        self.battery_module = Battery(self, self.__battery_callback)
        self.oxygen_module = Oxygen(self, self.__oxygen_callback)
        self.heartbeat = Heartbeat(self)
        self.bridge = CvBridge()
        self.backend_commands = BackendCommands(self)

    def __streaming_callback(self, data):
        self.get_logger().info('Receiving video frame')
        
        current_frame = self.bridge.imgmsg_to_cv2(data)
        model = YOLO("./yolo.pt")
        result = model.predict(current_frame, conf=0.6)
        annotated = result[0].plot()
        cv2.imshow("camera", annotated)
        cv2.waitKey(1)

    def __heartbeat_response_callback(self, data):
        self.backend_commands.send({'command': 'START', 'body': ''})

        #self.sio.emit("streaming", converted_string)
        # self.get_logger().info(f"Received message: {msg}")
        
    def __battery_callback(self, data):  
        self.percentage = ((data.voltage - 11)/1.6) * 100
        #print(self.percentage)
        return self.percentage
        
        
    def __oxygen_callback(self, data):
        print(data.data)
        
        
      
        
# def main(args=None):
#     rclpy.init(args=args)
#     image_subscriber = BackendController()
#     rclpy.spin(image_subscriber)
#     image_subscriber.destroy_node()
#     rclpy.shutdown()
  
# if __name__ == '__main__':
#   main()
        
        
        
        
        
        
      