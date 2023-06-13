import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan as LaserScanData
from modules.publishers import Velocity, Camera, HeartbeatResponse, TVOC, Temperature, ECO2, GPS
from modules.subscribers import Position, EulerData, Lidar, Imu, ImuData, DistanceFilterType, Heartbeat, BackendCommands

# from ros2_message_converter import message_converter
import json
from enum import Enum


class State(Enum):
    FOWARD = 1
    DETOUR_LEFT = 2
    DETOUR_RIGHT = 3


class TurtleBotController(Node):
    __euler_data = EulerData()
    __imu_data = ImuData()

    __velocity_module = None
    __position_module = None
    __lidar_module = None
    __camera_module = None

    __state = State.FOWARD

    def __init__(self):
        super().__init__("turtlebot_controller")

        self.__velocity_module = Velocity(self)
        self.__camera_module = Camera(self)
        self.__heartbeat_response_callback = HeartbeatResponse(self)

        self.__tvoc_sensor = TVOC(self)
        self.__temperature_sensor = Temperature(self)
        self.__eco2_sensor = ECO2(self)
        self.__gps_sensor = GPS(self)

        self.__position_module = Position(self, self.__position_callback)
        self.__lidar_module = Lidar(self, self.__lidar_callback)
        self.__imu_module = Imu(self, self.__imu_callback)
        self.__heartbeat_module = Heartbeat(self, self.__heartbeat_callback)
        self.__backend_commands_module = BackendCommands(
            self, self.__backend_commands_callback)

        self.command_start()  # If you want to start the robot automatically

    def command_start(self):
        self.get_logger().info("Starting robot runtime...")
        self.create_timer(1, self.__sensores_runtime)
        self.create_timer(0.16, self.__runtime_camera)
        self.create_timer(0.24, self.__runtime_movement)

    def __backend_commands_callback(self, data):
        print(data)
        msg_json = json.loads(data.data)
        match (msg_json["command"]):
            case "START":
                self.command_start()
            case "STOP":
                pass
            case "PAUSE":
                pass
            case "RESUME":
                pass
            case "RESTART":
                pass
            case "SHUTDOWN":
                pass

    def __heartbeat_callback(self, msg):
        print("Mensagem recebida com sucesso no heartbeat!")
        self.__heartbeat_response_callback.send("oie")

    def __position_callback(self, euler_data: EulerData):
        self.__euler_data = euler_data
        # self.get_logger().info(str(euler_data))

    def __lidar_callback(self, lidar_data: LaserScanData):
        # lidar_data.ranges = array of 360 values (0-360 degrees) of distance in meters
        # self.get_logger().info(str(lidar_data.ranges))
        pass

    def __imu_callback(self, imu_data: ImuData):
        self.__imu_data = imu_data
        # self.get_logger().info(str(imu_data))

    def __sensores_runtime(self):
        self.__tvoc_sensor.update()
        self.__temperature_sensor.update()
        self.__eco2_sensor.update()
        self.__gps_sensor.update()

    def __runtime_camera(self):
        self.__camera_module.update()

    def __runtime_movement(self):
        pass

        # frontal_min_distance = self.__lidar_module.frontal_distance(DistanceFilterType.MIN)
        # self.get_logger().info(f"Frontal distance: {frontal_min_distance}")

        # if frontal_min_distance < 0.3:
        #     _, left_avarage_distance, right_avarage_distance, _ = self.__lidar_module.average_distances

        #     if right_avarage_distance > left_avarage_distance and self.__state != State.DETOUR_LEFT:
        #         self.__state = State.DETOUR_RIGHT
        #         self.__velocity_module.apply(0, -0.30)

        #     if left_avarage_distance > right_avarage_distance and self.__state != State.DETOUR_RIGHT:
        #         self.__state = State.DETOUR_LEFT
        #         self.__velocity_module.apply(0, 0.30)
        # else:
        #     self.__state = State.FOWARD
        #     self.__velocity_module.apply(0.30, 0)

        # self.get_logger().info(f"State: {self.__state}")


if __name__ == "__main__":
    rclpy.init()
    node = TurtleBotController()
    rclpy.spin(node)
    rclpy.shutdown()
