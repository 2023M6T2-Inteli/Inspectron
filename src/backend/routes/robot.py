## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter, Depends  # Import APIRouter
from models import Robot
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel
from middlewares import JWTBearer

# Instanciando o objeto "router" da classe "APIRouter"
router = APIRouter()


# Definindo a rota "/robots"
@router.get(
    "/robots",
    dependencies=[Depends(JWTBearer())],
)
async def get_robots():
    robots = json.loads(Robot.objects().to_json())
    return JSONResponse(content=robots)


class robotModel(BaseModel):
    name: str
    ip: str


# Criando uma rota para salvar os robôs no banco de dados
@router.post(
    "/robots/create",
    dependencies=[Depends(JWTBearer())],
)
async def create_robot(robotBody: robotModel):
    robot = Robot(name=robotBody.name, ip=robotBody.ip)
    robot.save()
    robot_json = json.loads(robot.to_json())

    return JSONResponse(content=robot_json)
