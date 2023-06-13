#File onde é realizada a criação e o salvamento de três classes,
# Location, Robot e Scan em um banco de dados MongoDB, 
# estabelecendo as associações adequadas entre eles.

from mongoengine import * # Importando o módulo "mongoengine" / "mongoengine" é um módulo que permite a conexão com o banco de dados MongoDB
from models import Robot, Scan, Location # Importando a classe "Location" da pasta "models" e o arquivo "location.py"
from config import connect_to_database # Importando a variável "uri" do arquivo "db_connection.py" da pasta "config"
#Uri é a variável que contém a string de conexão com o banco de dados MongoDB
from bson import ObjectId

connect_to_database() # Conectando com o banco de dados MongoDB

location = Location(name="Atelie 06") # Instanciando o objeto "location" da classe "Location" e passando o parâmetro "name"
location.coordinates = {"x": 1, "y": 2} # Atribuindo o valor do parâmetro "coordinates" ao objeto "location"
location.save() # Salvando o objeto "location" no banco de dados

robot = Robot(name="Tortas") # Instanciando o objeto "robot" da classe "Robot" e passando o parâmetro "name"
robot.ip = '222.1312.1212' # Atribuindo o valor do parâmetro "ip" ao objeto "robot"
robot.save() # Salvando o objeto "robot" no banco de dados

# Instanciando o objeto "scan" da classe "Scan" e passando o parâmetro "directions"
scan = Scan()
scan.actions = [{"x": 1, "y": 2}, 10, 'ANDOU PRA ESQUERDA', 20]
scan.oxygen = 22.2
scan.location = location.id
scan.robot = robot.id
scan.save()
