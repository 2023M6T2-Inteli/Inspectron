import rclpy
from rclpy.node import Node
from ultralytics import YOLO
import cv2
from cv_bridge import CvBridge
from ros.subscribers import HeartbeatResponse, Battery, Oxygen, Camera, Humidity, Temperature
from ros.publisher import BackendCommands, Heartbeat
import base64

class BackendController(Node):
    def __init__(self, sio, event_queue):
        super().__init__("backend_controller")
        self.sio = sio
        self.camera_module = Camera(self, self.__camera_callback)
        self.heartbeat_response_module = HeartbeatResponse(self, self.__heartbeat_response_callback)
        self.battery_module = Battery(self, self.__battery_callback)
        self.oxygen_module = Oxygen(self, self.__oxygen_callback)
        self.temperature_module = Temperature(self, self.__temperature_callback)
        self.humidity_module = Humidity(self, self.__humidity_callback)
        
        self.heartbeat = Heartbeat(self)
        self.backend_commands = BackendCommands(self)
        
        self.bridge = CvBridge()
        self.event_queue = event_queue
        self.teste = 0
        
        

    async def __camera_callback(self, data):
        self.get_logger().info('Receiving video frame')
        
        current_frame = self.bridge.imgmsg_to_cv2(data, desired_encoding="bgr8")

        model = YOLO("ros/yolo.pt")
        result = model.predict(current_frame, conf=0.6)
        annotated = result[0].plot()

        _, buffer = cv2.imencode('.jpg', annotated)

        # Convert byte array to base64 string
        frame64 = base64.b64encode(buffer).decode('utf-8')
        event = {"name": "camera", "data": frame64}
        self.event_queue.put(event)
        self.teste += 1
        print(self.teste, flush=True)
        
    def __heartbeat_response_callback(self, data):
        self.backend_commands.send({'command': 'START', 'body': ''})
           
          
    def __battery_callback(self, data):  
        self.percentage = ((data.voltage - 11)/1.6) * 100
        event = {"name": "battery", "data": self.percentage}
        self.event_queue.put(event)
        #print(self.percentage)
                     
    def __oxygen_callback(self, data):
        print(data.data)
        event = {"name": "oxygen", "data": data.data}
        self.event_queue.put(event)
        
    def __temperature_callback(self, data):
        print(data.data)
        event = {"name": "temperature", "data": data.data}
        self.event_queue.put(event)

    
    def __humidity_callback(self, data):
        print(data.data)
        event = {"name": "humidity", "data": data.data}
        self.event_queue.put(event)
        
        
        
      
        
# def main(args=None):
#     rclpy.init(args=args)
#     image_subscriber = BackendController()
#     rclpy.spin(image_subscriber)
#     image_subscriber.destroy_node()
#     rclpy.shutdown()
  
# if __name__ == '__main__':
#   main()
        
        
        
        
        
        
 
      

    
