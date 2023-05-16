from mongoengine import *
from enum import Enum
from ..models.location import Location
from ..models.robot import Robot


class Direction(Enum):
    FRENTE = 1
    TRAS = 2
    DIREITA = 3
    ESQUERDA = 4


class Scan(Document):
    directions = ListField(required=True,
                           fields={
                               "direction": EnumField(Direction, default=Direction.FRENTE),
                               "value": IntField()
                           })
    oxygen = FloatField()
    location = ReferenceField('Location')
    robot = ReferenceField('Robot')
