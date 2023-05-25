#File onde é realizada o delete de três classes,
# Location, Robot e Scan em um banco de dados MongoDB, 
# estabelecendo as associações adequadas entre eles.

from mongoengine import * ## Importando o módulo "mongoengine" / "mongoengine" é um módulo que permite a conexão com o banco de dados MongoDB
from ..models.location import Location # Importando a classe "Location" da pasta "models" e o arquivo "location.py"
from ..models.robot import Robot # Importando a classe "Robot" da pasta "models" e o arquivo "robot.py"
from ..models.scan import Direction # Importando a classe "Direction" da pasta "models" e o arquivo "scan.py"
from ..models.scan import Scan # Importando a classe "Scan" da pasta "models" e o arquivo "scan.py"
from ..config.db_connection import uri # Importando a variável "uri" do arquivo "db_connection.py" da pasta "config"

connect(host=uri) # Conectando com o banco de dados MongoDB

location = Location.objects(name="Atelie 09").delete() # Deletando o objeto "location" do banco de dados

robot = Robot.objects(name="Tortuguita").delete() # Deletando o objeto "robot" do banco de dados

scan = Scan.objects(_id=).delete() # Deletando o objeto "scan" do banco de dados
