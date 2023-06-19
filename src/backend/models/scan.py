from mongoengine import *

class Scan(Document):
    actions = ListField(DynamicField())
    name = StringField()
    oxygen_min = FloatField()
    oxygen_max = FloatField()
    temperature_min = FloatField()
    temperature_max = FloatField()
    humidity_min = FloatField()
    humidity_max = FloatField()
    location = ObjectIdField()
    robot = ObjectIdField()
    created_at = DateTimeField()

