import rclpy
from rclpy.node import Node
from modules.publishers import Oxygen

class TurtleBotController(Node):
   
    def __init__(self):
        super().__init__("turtlebot_controller")

        self.oxygen_callback = Oxygen(self)
        self.create_timer(1, self.__runtime)
        
        
    def __runtime(self):
        print('ok')
        self.oxygen_callback.send(1.6)

            
    def __oxygen_runtime(self):
        #leitura do sensor
         #Passar informação lida
        pass
        
        


if __name__ == "__main__":
    rclpy.init()
    node = TurtleBotController()
    rclpy.spin(node)
    rclpy.shutdown()