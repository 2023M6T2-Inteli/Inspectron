## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter, Depends  # Import APIRouter
from models import Location
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel
from middlewares import JWTBearer
from models import Scan

# Instanciando o objeto "router" da classe "APIRouter"
router = APIRouter()  

# Definindo a rota "/locations" para o método "get_locations"
@router.get("/locations", dependencies=[Depends(JWTBearer())],)
async def get_locations():  # Definindo o método "get_locations"/ o "async" é para que o método seja assíncrono
    locations = json.loads(Location.objects().to_json())

    # get all scans that happened in every location
    for location in locations:
        scans = json.loads(
            Scan.objects(location=location["_id"]["$oid"]).to_json()
        )
        location["scans"] = scans

    
    # Retornando o objeto "locations" em formato JSON
    return JSONResponse(content=locations)


class LocationModel(BaseModel):
    name: str
    coordinates: dict[str, float]

# Definindo a rota "/locations/create" para o método "create_location"
@router.post("/locations/create", dependencies=[Depends(JWTBearer())],)
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

