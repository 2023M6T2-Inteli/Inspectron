from mongoengine import *
from ..models.location import Location
from ..models.robot import Robot
from ..models.scan import Direction
from ..models.scan import Scan
from ..config.db_connection import uri

connect(host=uri)

location = Location.objects(name="Atelie 09").delete()

robot = Robot.objects(name="Tortuguita").delete()

scan = Scan.objects(_id=).delete()
