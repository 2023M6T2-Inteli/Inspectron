import rclpy
from rclpy.node import Node
from ultralytics import YOLO
import cv2
from cv_bridge import CvBridge
from subscribers import Streaming

class BackendController(Node):
    def __init__(self):
        super().__init__("backend_controller")
        # self.sio = sio
        self.streaming_module = Streaming(self, self.__streaming_callback)
        self.bridge = CvBridge()

    def __streaming_callback(self, data):
        self.get_logger().info('Receiving video frame')
        
        current_frame = self.bridge.imgmsg_to_cv2(data)
        model = YOLO("./yolo.pt")
        result = model.predict(current_frame, conf=0.6)
        annotated = result[0].plot()
        cv2.imshow("camera", annotated)
        
      
        
def main(args=None):
    rclpy.init(args=args)
    image_subscriber = BackendController()
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
  main()
        
        
        
        
        
        
        
        
        #cv2.waitKey(1)
        
        # #Converte de base64 para imagem
        # decoded_data=base64.b64decode(msg)
        
        # #Passa pelo modelo preditivo
        # model = YOLO("./yolo.pt")
        # result = model.predict(decoded_data, conf=0.4)
        # annotated_frame = result[0].plot()

        # #Converte novamente para base64
        # converted_string = base64.b64encode(annotated_frame) 

        # self.sio.emit("streaming", converted_string)
        # self.get_logger().info(f"Received message: {msg}")