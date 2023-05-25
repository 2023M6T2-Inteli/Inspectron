## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter # Import APIRouter
from ..models.location import Location # Importando a classe "Location" da pasta "models" e o arquivo "location.py"
from ..models.robot import Robot # Importando a classe "Robot" da pasta "models" e o arquivo "robot.py"
from ..models.scan import Scan # Importando a classe "Scan" da pasta "models" e o arquivo "scan.py"

router = APIRouter() # Instanciando o objeto "router" da classe "APIRouter"

@router.get('/locations') # Definindo a rota "/locations" para o método "get_locations" 
async def get_locations():  # Definindo o método "get_locations"/ o "async" é para que o método seja assíncrono
    locations = Location.objects() # Instanciando o objeto "locations" da classe "Location" e o método "objects" para retornar todos os objetos da classe
    return locations.to_json() # Retornando o objeto "locations" em formato JSON

@router.post('/locations/create') # Definindo a rota "/locations/create" para o método "create_location"
async def create_location(body): # Definindo a função "create_location" com o parâmetro "body" / body é o corpo da requisição
    location = Location(name=body['name'], coordinates=body['coordinates']) # Instanciando o objeto "location" da classe "Location" e passando os parâmetros "name" e "coordinates" do corpo da requisição
    location.save() # Salvando o objeto "location" no banco de dados
    return location.to_json() # Retornando o objeto "location" em formato JSON

# Definindo a rota "/robots"
@router.get('/robot')
async def get_robots():
    robots = Robot.objects()
    return robots.to_json()

# Definindo a rota "/robots/create" 
#Criando uma rota para salvar os robôs no banco de dados
@router.post('/robot/create')
async def get_robots(body):
    robot = Robot(name=body['name'], ip=body['ip'])
    robot.save()
    return robot.to_json()

# Definindo a rota "/scan"
@router.get('/scan')
async def get_scans():
    scans = Scan.objects()
    return scans.to_json()