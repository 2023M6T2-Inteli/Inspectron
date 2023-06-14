import rclpy
from rclpy.node import Node
from std_msgs.msg._float64 import Float64


class Controller(Node):
    def __init__(self):
        super().__init__("turtlebot")
        self.publisher_temperature = self.create_publisher(Float64, '/temperature', 10)
        self.publisher_oxygen = self.create_publisher(Float64, '/oxygen', 10)
        self.publisher_battery = self.create_publisher(Float64, '/battery', 10)
        self.timer = self.create_timer(0.1, self.publish)
        
        
    def publish(self):                  
        self.publisher_temperature.publish(Float64(data=float(0.16)))
        self.publisher_oxygen.publish(Float64(data=float(0.16)))
        self.publisher_oxygen.publish(Float64(data=float(11.5)))

        print("ok")
            

def main(args=None):
    rclpy.init(args=args)
    subscriebr_node = Controller()
    rclpy.spin(subscriebr_node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()