#File onde é realizada a criação e o salvamento de três classes,
# Location, Robot e Scan em um banco de dados MongoDB, 
# estabelecendo as associações adequadas entre eles.

from mongoengine import * # Importando o módulo "mongoengine" / "mongoengine" é um módulo que permite a conexão com o banco de dados MongoDB
from ..models.location import Location # Importando a classe "Location" da pasta "models" e o arquivo "location.py"
from ..models.robot import Robot # Importando a classe "Robot" da pasta "models" e o arquivo "robot.py"
from ..models.scan import Direction # Importando a classe "Direction" da pasta "models" e o arquivo "scan.py"
from ..models.scan import Scan # Importando a classe "Scan" da pasta "models" e o arquivo "scan.py"
from ..config.db_connection import uri # Importando a variável "uri" do arquivo "db_connection.py" da pasta "config"
#Uri é a variável que contém a string de conexão com o banco de dados MongoDB

connect(host=uri) # Conectando com o banco de dados MongoDB

location = Location(name="Atelie 09") # Instanciando o objeto "location" da classe "Location" e passando o parâmetro "name"
location.coordinates = {"x": 1, "y": 2} # Atribuindo o valor do parâmetro "coordinates" ao objeto "location"
location.save() # Salvando o objeto "location" no banco de dados

robot = Robot(name="Tortuguita") # Instanciando o objeto "robot" da classe "Robot" e passando o parâmetro "name"
robot.ip = 77777777 # Atribuindo o valor do parâmetro "ip" ao objeto "robot"
robot.save() # Salvando o objeto "robot" no banco de dados

# Instanciando o objeto "scan" da classe "Scan" e passando o parâmetro "directions"
scan = Scan(directions=[{"direction": Direction.FRENTE, "value": 10}, {
            "direction": Direction.DIREITA, "value": 30}, {"direction": Direction.TRAS, "value": 20}])
scan.oxygen = 22.2
scan.location = location
scan.robot = robot
scan.save()
