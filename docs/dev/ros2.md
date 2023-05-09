# ROS2

### Conventions:

-   For all topics, services, and parameters, the name should be prefixed with `/turtlebot/` to avoid name collisions.
-   Use `snake_case` for all names.
-   Services: before name, use `call_` to indicate that it is a service call and `set_` to indicate that it is a service set.

## Robot

### Subscribed:

### Publishers:

-   `/turtlebot/camera_stream → { CameraImageBuffer }`
-   `/turtlebot/lidar → { Array[Degrees, Distance]`
-   `/turtlebot/state → { Enum[ROTATING, MOVING, STOPPED...}`
-   `/turtlebot/imu → { Position { X Y Z } Acceleration { X Y Z } }`
-   `/turtlebot/oxygen → { QualityPercent }`
-   `/turtlebot/battery → { Percent }`

### Services:

-   `/turtlebot/call_rotate ← { Degrees, Speed }`

    -   Parameters: `Degrees` is in the range of `[-360, 360]`, `-360` is full reverse, and `360` is full forward. `Speed` is in the range of `[0, 100]`, where `0` is stopped, and `100` is full speed.
    -   Return: None

-   `/turtlebot/set_motor ← { MotorA MotorB }`
    -   Parameters: `MotorA` and `MotorB` are in the range of `[-100, 100]`, where `0` is stopped, `-100` is full reverse, and `100` is full forward.
    -   Return: None

### Parameters:

## Backend / Controller

### Subscribed:

-   `/turtlebot/camera_stream ← { CameraImageBuffer }`
-   `/turtlebot/lidar ← { Array[Degrees, Distance]`
-   `/turtlebot/state ← { Enum[ROTATING, MOVING, STOPPED}`
-   `/turtlebot/imu ← { Position { X Y Z } Acceleration { X Y Z } }`
-   `/turtlebot/oxygen ← { QualityPercent }`
-   `/turtlebot/battery ← { Percent }`

### Publishers:

### Clients:

#### Inner calls:

-   `/turtlebot/call_rotate → { Degrees, Speed }`

    -   Parameters: `Degrees` is in the range of `[-360, 360]`, `-360` is full reverse, and `360` is full forward. `Speed` is in the range of `[0, 100]`, where `0` is stopped, and `100` is full speed.
    -   Return: None

-   `/turtlebot/call_move` → { Movement { MotorA, MotorB, Time} }

#### Manual sets:

-   `/turtlebot/set_motor → { MotorA MotorB }`
    -   Parameters: `MotorA` and `MotorB` are in the range of `[-100, 100]`, where `0` is stopped, `-100` is full reverse, and `100` is full forward.
    -   Return: None

### Parameters:
