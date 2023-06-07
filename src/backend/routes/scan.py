## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter, Depends  # Import APIRouter
from models import Scan, Location, Robot
from fastapi.responses import JSONResponse
import json
from middlewares import JWTBearer
from bson import ObjectId

# Instanciando o objeto "router" da classe "APIRouter"
router = APIRouter()

def complete_scan(location=None):
    scans = Scan.objects()
    for scan in scans:
        location = Location.objects(id=scan.location).first()
        robot = Robot.objects(id=scan.robot).first()

        scan_data = json.loads(scan.to_json())
        location_data = json.loads(location.to_json())
        robot_data = json.loads(robot.to_json())

        scan_data["location"] = location_data
        scan_data["robot"] = robot_data

    return scan_data

# Definindo a rota "/scan"
@router.get(
    "/scans",
    dependencies=[Depends(JWTBearer())],
)
async def get_scans():
    scan_data = complete_scan()
    json.dumps(scan_data)
    return JSONResponse(content=scan_data)

@router.get(
    "/scans/location/{location_id}"
)
async def get_scans_by_location(location_id: str):
    location = Location.objects(id=ObjectId(location_id)).first()
    scans = complete_scan(location=location.id)

    return JSONResponse(content=scans)
