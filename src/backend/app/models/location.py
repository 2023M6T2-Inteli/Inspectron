from mongoengine import *

connect('Inspectron')

class location(Document):
    name = StringField(required=True)
    coordinates = DictField(required=True,
        fields ={
            "x": FloatField(),
            "y": FloatField()
        })
