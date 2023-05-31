from mongoengine import *

# Criando uma tabela as localizações
class User(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)
