## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter  # Import APIRouter
from models import Robot, Scan, Location
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel

# Instanciando o objeto "router" da classe "APIRouter"
router = APIRouter()  

# Definindo a rota "/locations" para o método "get_locations"
@router.get("/locations")
async def get_locations():  # Definindo o método "get_locations"/ o "async" é para que o método seja assíncrono
    locations = json.loads(Location.objects().to_json())
    
    # Retornando o objeto "locations" em formato JSON
    return JSONResponse(content=locations)


class LocationModel(BaseModel):
    name: str
    coordinates: dict[str, float]


# Definindo a rota "/locations/create" para o método "create_location"
@router.post("/locations/create")
async def create_location(
    locationBody: LocationModel,
):
    # Instanciando o objeto "location" da classe "Location" e passando os parâmetros "name" e "coordinates" do corpo da requisição
    location = Location(name=locationBody.name, coordinates=locationBody.coordinates)

    # Salvando o objeto "location" no banco de dados
    location.save()
    location_json = json.loads(location.to_json())

    # Retornando o objeto "location" em formato JSON
    return JSONResponse(content=location_json)


# Definindo a rota "/robots"
@router.get("/robots")
async def get_robots():
    robots = json.loads(Robot.objects().to_json())
    return JSONResponse(content=robots)


class robotModel(BaseModel):
    name: str
    ip: str

# Criando uma rota para salvar os robôs no banco de dados
@router.post("/robots/create")
async def get_robots(robotBody: robotModel):
    robot = Robot(name=robotBody.name, ip=robotBody.ip)
    robot.save()
    robot_json = json.loads(robot.to_json())

    return JSONResponse(content=robot_json)


# Definindo a rota "/scan"
@router.get("/scans")
async def get_scans():
    scans = Scan.objects()
    for scan in scans:
        location = Location.objects(id=scan.location).first()
        robot = Robot.objects(id=scan.robot).first()

        scan_data = json.loads(scan.to_json())
        location_data = json.loads(location.to_json())
        robot_data = json.loads(robot.to_json())

        scan_data["location"] = location_data
        scan_data["robot"] = robot_data

        json.dumps(scan_data)

    return JSONResponse(content=scan_data)
