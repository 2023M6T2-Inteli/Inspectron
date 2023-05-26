from mongoengine import *

class Robot(Document):
    name = StringField(required=True)
    ip = StringField(required=True)