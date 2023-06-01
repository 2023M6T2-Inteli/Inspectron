## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter, HTTPException  # Import APIRouter
from models import User
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel
from utils import (
    hashPassword,
    verifyPassword,
    create_access_token,
    create_refresh_token,
)

# Instanciando o objeto "router" da classe "APIRouter"
router = APIRouter()


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

    hashed_password = hashPassword(userBody.password)
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
        if verifyPassword(userBody.password, user[0]["password"]):
            response = {
                "access_token": create_access_token(user[0]["email"]),
                "refresh_token": create_refresh_token(user[0]["email"]),
                **user[0],
            }
            return JSONResponse(content=response)
        else:
            raise HTTPException(status_code=500, detail="Senha incorreta")
    else:
        raise HTTPException(status_code=500, detail="Usuário não encontrado")
