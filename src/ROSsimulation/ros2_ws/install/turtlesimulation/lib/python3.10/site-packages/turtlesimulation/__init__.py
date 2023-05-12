#! /usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtleController(Node):
    
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic="/cmd_vel",
            qos_profile=10
        )
        timer_period = 0.5
        self.timer = self.create_timer(
                timer_period_sec=timer_period,
                callback=self.timer_callback
        )

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.angular.z = 1.0
        self.publisher.publish(msg)
        self.get_logger().info("Publicando velocidades para a tortuguita")

def main(args=None):
    rclpy.init(args=args)
    tc = TurtleController()
    rclpy.spin(tc)
    tc.destroy_node()
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()