## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter, HTTPException  # Import APIRouter
from models import Robot, Scan, Location, User
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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
async def create_robot(robotBody: robotModel):
    robot = Robot(name=robotBody.name, ip=robotBody.ip)
    robot.save()
    robot_json = json.loads(robot.to_json())

    return JSONResponse(content=robot_json)


# Definindo a rota "/scan"
@router.get("/scans")
async def get_scans():
    scans = json.loads(Scan.objects().to_json())
    
    return JSONResponse(content=scans)

class userModel(BaseModel):
    name: str
    email: str
    password: str

# Criando uma rota para salvar um usuário no banco de dados
@router.post("/users/create")
async def get_robots(userBody: userModel):

    user = json.loads(User.objects(email=userBody.email).to_json())
    if user:
        raise HTTPException(status_code=500, detail="Usuário já existe")

    hashed_password = pwd_context.hash(userBody.password)
    user = User(name=userBody.name, email=userBody.email, password=hashed_password)
    user.save()
    user_json = json.loads(user.to_json())

    return JSONResponse(content=user_json)

@router.get("/users")
async def get_users():
    users = json.loads(User.objects().to_json())
    
    return JSONResponse(content=users)

class loginModel(BaseModel):
    email: str
    password: str

# Rota para logar um usuário
@router.post("/users/login")
async def login_user(userBody: loginModel):
    user = json.loads(User.objects(email=userBody.email).to_json())
    if user:
        if pwd_context.verify(userBody.password, user[0]['password']):
            return JSONResponse(content=user[0])
        else:
            raise HTTPException(status_code=500, detail="Senha incorreta")
    else:
        raise HTTPException(status_code=500, detail="Usuário não encontrado")