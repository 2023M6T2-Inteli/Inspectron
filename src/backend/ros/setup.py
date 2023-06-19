import rclpy
from rclpy.node import Node
from ultralytics import YOLO
import cv2
from cv_bridge import CvBridge
from ros.subscribers import HeartbeatResponse, Battery, Tvoc, Camera, Humidity, Temperature, GPS, Eco2
from ros.publisher import BackendCommands, Heartbeat
import base64
import asyncio
from utils import NewScan

class BackendController(Node):
    def __init__(self, sio, event_queue, new_scan):
        super().__init__("backend_controller")
        self.sio = sio

        # Subscribers
        self.camera_module = Camera(self, self.__camera_callback)
        self.heartbeat_response_module = HeartbeatResponse(self, self.__heartbeat_response_callback)
        self.battery_module = Battery(self, self.__battery_callback)
        self.tvoc_module = Tvoc(self, self.__tvoc_callback)
        self.temperature_module = Temperature(self, self.__temperature_callback)
        self.humidity_module = Humidity(self, self.__humidity_callback)
        self.gps_module = GPS(self, self.__gps_callback)
        self.eco2_module = Eco2(self, self.__eco2_callback)
        
        # Publishers
        self.heartbeat = Heartbeat(self)
        self.backend_commands = BackendCommands(self)
        
        self.bridge = CvBridge()
        self.event_queue = event_queue

        self.new_scan = new_scan

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
        
    def __heartbeat_response_callback(self, data):
        self.backend_commands.send({'command': 'START', 'body': ''})
        self.new_scan.heartbeat = data
           
          
    def __battery_callback(self, data):  
        self.percentage = ((data.data - 11)/1.6) * 100
        event = {"name": "battery", "data": self.percentage}
        self.event_queue.put(event)
        self.new_scan.battery = self.percentage
                     
    def __tvoc_callback(self, data):
        self.update_range("tvoc_max", "tvoc_min", data.data)
        event = {"name": "tvoc", "data": data.data}
        self.event_queue.put(event)
        
    def __temperature_callback(self, data):
        self.update_range("temperature_max", "temperature_min", data.data)
        event = {"name": "temperature", "data": data.data}
        self.event_queue.put(event)
    
    def __humidity_callback(self, data):
        self.update_range("humidity_max", "humidity_min", data.data)
        event = {"name": "humidity", "data": data.data}
        self.event_queue.put(event)

    def __gps_callback(self, data):
        print(data.data, flush=True)
        event = {"name": "gps", "data": data.data}
        self.event_queue.put(event)

    def __eco2_callback(self, data):
        self.update_range("eco2_max", "eco2_min", data.data)
        event = {"name": "eco2", "data": data.data}
        self.event_queue.put(event)
        
    def update_range(self, fieldMax, fieldMin, data):
        if self.new_scan[fieldMax] == None:
            self.new_scan[fieldMax] = data
        elif data > self.new_scan[fieldMax]:
            self.new_scan[fieldMax] = data

        if self.new_scan[fieldMin] == None:
            self.new_scan[fieldMin] = data
        elif data < self.new_scan[fieldMin]:
            self.new_scan[fieldMin] = data