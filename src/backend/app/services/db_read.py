from mongoengine import *
from ..models.location import Location
from ..models.robot import Robot
from ..models.scan import Direction
from ..models.scan import Scan
from ..config.db_connection import uri

connect(host=uri)

locations = Location.objects()

for location in locations:
    print(location.to_json())
