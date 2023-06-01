from mongoengine import *
from enum import IntEnum


# Criando uma tabela para os scans

class Direction(IntEnum):
    FRENTE = 1
    TRAS = 2
    DIREITA = 3
    ESQUERDA = 4


class Scan(Document):
    directions = ListField(DictField(required=True,
                           fields={
                               "direction": EnumField(Direction),
                               "value": IntField()
                           }))
    oxygen = FloatField()
    location = ObjectIdField()
    robot = ObjectIdField()
