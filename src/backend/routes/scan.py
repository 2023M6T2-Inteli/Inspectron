## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter, Depends  # Import APIRouter
from models import Scan
from fastapi.responses import JSONResponse
import json
from middlewares import JWTBearer

# Instanciando o objeto "router" da classe "APIRouter"
router = APIRouter()


# Definindo a rota "/scan"
@router.get(
    "/scans",
    dependencies=[Depends(JWTBearer())],
)
async def get_scans():
    scans = json.loads(Scan.objects().to_json())

    return JSONResponse(content=scans)
