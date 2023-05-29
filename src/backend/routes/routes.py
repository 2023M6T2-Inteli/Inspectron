## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter  # Import APIRouter
from models import Robot, Scan, Location
from fastapi.responses import JSONResponse
import json
from config import Console

router = APIRouter()  # Instanciando o objeto "router" da classe "APIRouter"


@router.get("/locations")  # Definindo a rota "/locations" para o método "get_locations"
async def get_locations():  # Definindo o método "get_locations"/ o "async" é para que o método seja assíncrono
    Console.log("diahdiwa")
    locations = json.loads(Location.objects().to_json())
    # Instanciando o objeto "locations" da classe "Location" e o método "objects" para retornar todos os objetos da classe
    return JSONResponse(
        content=locations
    )  # Retornando o objeto "locations" em formato JSON


# Definindo a rota "/locations/create" para o método "create_location"
@router.post("/locations/create")
async def create_location(
    body,
):
    Console.log("djaihdbadhao")
    location = Location(
        name=body["name"], coordinates=body["coordinates"]
    )  # Instanciando o objeto "location" da classe "Location" e passando os parâmetros "name" e "coordinates" do corpo da requisição
    location.save()  # Salvando o objeto "location" no banco de dados
    location_json = json.loads(location.to_json())
    return JSONResponse(
        content=location_json
    )  # Retornando o objeto "location" em formato JSON


# Definindo a rota "/robots"
@router.get("/robot")
async def get_robots():
    robots = json.loads(Robot.objects().to_json())
    return JSONResponse(content=robots)


# Definindo a rota "/robots/create"
# Criando uma rota para salvar os robôs no banco de dados
@router.post("/robot/create")
async def get_robots(body):
    robot = Robot(name=body["name"], ip=body["ip"])
    robot.save()
    robot_json = json.loads(robot.to_json())

    return JSONResponse(content=robot_json)


# Definindo a rota "/scan"
@router.get("/scan")
async def get_scans():
    scans = json.loads(Scan.objects().to_json())
    return JSONResponse(content=scans)
