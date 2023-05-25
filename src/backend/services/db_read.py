from mongoengine import * # Importando o módulo "mongoengine" / "mongoengine" é um módulo que permite a conexão com o banco de dados MongoDB
from ..models.location import Location # Importando a classe "Location" da pasta "models" e o arquivo "location.py"
from ..models.robot import Robot # Importando a classe "Robot" da pasta "models" e o arquivo "robot.py"
from ..models.scan import Direction # Importando a classe "Direction" da pasta "models" e o arquivo "scan.py"
from ..models.scan import Scan # Importando a classe "Scan" da pasta "models" e o arquivo "scan.py"
from ..config.db_connection import uri # Importando a variável "uri" do arquivo "db_connection.py" da pasta "config"

connect(host=uri) # Conectando com o banco de dados MongoDB

locations = Location.objects() # Atribuindo o valor do objeto "Location" à variável "locations"

for location in locations: # Para cada objeto "location" em "locations"
    print(location.to_json()) # Imprimindo o objeto "location" em formato JSON
