from mongoengine import *


# Criando uma tabela para os robos
class Robot(Document):
    name = StringField(required=True)
    ip = IntField(required=True)