from mongoengine import *


class Location(Document):
    name = StringField(required=True)
    coordinates = DictField(required=True,
                            fields={
                                "x": FloatField(required=True),
                                "y": FloatField(required=True)
                            })
