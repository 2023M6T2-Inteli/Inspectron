import rclpy
from rclpy.node import Node
from std_msgs.msg._float64 import Float64
from std_msgs.msg._string import String
import json

class Controller(Node):
    def __init__(self):
        super().__init__("turtlebot")
        self.publisher_tvoc = self.create_publisher(Float64, '/tvoc', 10)
        self.publisher_temperature = self.create_publisher(Float64, '/temperature', 10)
        self.publisher_eco2 = self.create_publisher(Float64, '/eco2', 10)
        self.publisher_gps = self.create_publisher(String, '/gps', 1000)
       # self.publisher_battery = self.create_publisher(Float64, '/battery', 10)
        self.timer = self.create_timer(0.1, self.publish)
        print("ok")
        
    def publish(self):                  
        self.publisher_temperature.publish(Float64(data=float(0.32)))
        self.publisher_tvoc.publish(Float64(data=float(0.56)))
        self.publisher_eco2.publish(Float64(data=float(0.35)))
       # self.publisher_battery.publish(Float64(data=float(112.5)))

        gps_data = {
            'x': 53.0,
            'y': 21.0,
        }

        json_gps_data = json.dumps(gps_data)

        self.publisher_gps.publish(String(data=json_gps_data))

            

def main(args=None):
    rclpy.init(args=args)
    subscriebr_node = Controller()
    rclpy.spin(subscriebr_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
