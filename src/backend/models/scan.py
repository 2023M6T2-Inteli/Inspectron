from mongoengine import *

class Scan(Document):
    actions = ListField(DynamicField())
    name = StringField()
    tvoc_min = FloatField()
    tvoc_max = FloatField()
    eco2_min = FloatField()
    eco2_max = FloatField()
    temperature_min = FloatField()
    temperature_max = FloatField()
    humidity_min = FloatField()
    humidity_max = FloatField()
    location = ObjectIdField()
    robot = ObjectIdField()
    video_filename = StringField()
    created_at = DateTimeField()

