from mongoengine import *

class Scan(Document):
    actions = ListField(DynamicField())
    oxygen = FloatField()
    location = ObjectIdField()
    robot = ObjectIdField()
