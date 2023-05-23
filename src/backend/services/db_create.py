from mongoengine import *
from ..models.location import Location
from ..models.robot import Robot
from ..models.scan import Direction
from ..models.scan import Scan
from ..config.db_connection import uri

connect(host=uri)

location = Location(name="Atelie 09")
location.coordinates = {"x": 1, "y": 2}
location.save()

robot = Robot(name="Tortuguita")
robot.ip = 77777777
robot.save()

scan = Scan(directions=[{"direction": Direction.FRENTE, "value": 10}, {
            "direction": Direction.DIREITA, "value": 30}, {"direction": Direction.TRAS, "value": 20}])
scan.oxygen = 22.2
scan.location = location
scan.robot = robot
scan.save()
