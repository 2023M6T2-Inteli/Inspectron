from mongoengine import *

# Criando uma tabela as localizações
class Location(Document):
    name = StringField(required=True)
    coordinates = DictField(required=True,
                            fields={
                                "x": FloatField(required=True),
                                "y": FloatField(required=True)
                            })
