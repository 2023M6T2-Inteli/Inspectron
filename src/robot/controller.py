import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from sensor_msgs.msg import LaserScan as LaserScanData
from modules.publishers import Velocity, Camera, HeartbeatResponse, TVOC, ECO2, GPS
from modules.subscribers import Position, EulerData, Lidar, Imu, ImuData, DistanceFilterType, Heartbeat, BackendCommands
from sensors.environment import EnvironmentSensor
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

        # Publishers
        self.__tvoc_sensor = TVOC(self)
        self.__eco2_sensor = ECO2(self)
        self.__gps_sensor = GPS(self)

        # Subscribers
        self.__position_module = Position(self, self.__position_callback)
        self.__lidar_module = Lidar(self, self.__lidar_callback)
        self.__imu_module = Imu(self, self.__imu_callback)
        self.__heartbeat_module = Heartbeat(self, self.__heartbeat_callback)
        self.__backend_commands_module = BackendCommands(self, self.__backend_commands_callback)

        # Set runtime objects
        self.__sensores_runtime_object = None
        self.__runtime_camera_object = None
        self.__runtime_movement_object = None

		EnvironmentSensor.setup()

        self.__sensores_runtime_object = self.create_timer(1, self.__sensores_runtime)
        # self.__command_start()  # Uncomment to start robot runtime on startup

    def __command_start(self):
        self.get_logger().info("Starting robot runtime...")
        self.__runtime_movement_object = self.create_timer(0.08, self.__runtime_movement)
        self.__runtime_camera_object = self.create_timer(0.24, self.__runtime_camera)

    def __backend_commands_callback(self, data):
        msg_json = json.loads(data.data)
        match (msg_json["command"]):
            case "START":
                self.__command_start()

            case "STOP":
                runtimes = [self.__runtime_movement_object, self.__runtime_camera_object]

                for runtime in runtimes:
                    if runtime and (not runtime.is_canceled()):
                        runtime.cancel()

                self.__velocity_module.apply(0.0, 0.0)

    def __heartbeat_callback(self, msg):
        self.__heartbeat_response_callback.pong()

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
        if EnvironmentSensor.update_and_read_data():
            self.__tvoc_sensor.update()
            self.__eco2_sensor.update()

        self.__gps_sensor.update()

    def __runtime_camera(self):
        self.__camera_module.update()

    def __runtime_movement(self):
        frontal_min_distance, right_min_distance, left_min_distance, back_min_distance = self.__lidar_module.min_distances
        # self.get_logger().info(
        #    f"\nFrontal: {frontal_min_distance} \n Right: {right_min_distance} \n Left: {left_min_distance} \n Back: {back_min_distance}")

        if frontal_min_distance < 0.32:
            _, left_avarage_distance, right_avarage_distance, _ = self.__lidar_module.average_distances

            if right_avarage_distance > left_avarage_distance and self.__state != State.DETOUR_LEFT:
                self.__state = State.DETOUR_RIGHT
                self.__velocity_module.apply(0, 0.30)

            if left_avarage_distance > right_avarage_distance and self.__state != State.DETOUR_RIGHT:
                self.__state = State.DETOUR_LEFT
                self.__velocity_module.apply(0, -0.30)
        else:
            self.__state = State.FOWARD
            self.__velocity_module.apply(0.2, 0)

        # self.get_logger().info(f"State: {self.__state}")


if __name__ == "__main__":
    rclpy.init()
    node = TurtleBotController()
    rclpy.spin(node)
    rclpy.shutdown()
