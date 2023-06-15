## File principal do projeto, onde são definidas as rotas e os métodos

from fastapi import APIRouter, Depends  # Import APIRouter
from models import Scan, Location, Robot
from fastapi.responses import JSONResponse
import json
from middlewares import JWTBearer
from bson import ObjectId

# Instanciando o objeto "router" da classe "APIRouter"
router = APIRouter()

def complete_scan():
    scans = Scan.objects()
    all_scans = []
    for scan in scans:
        location = Location.objects(id=scan.location).first()
        robot = Robot.objects(id=scan.robot).first()

        scan_data = json.loads(scan.to_json())
        location_data = json.loads(location.to_json())
        robot_data = json.loads(robot.to_json())

        scan_data["location"] = location_data
        scan_data["robot"] = robot_data
        all_scans.append(scan_data)

    return all_scans

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
    location = Location.objects(id=location_id).first()
    scans = Scan.objects(location=location_id)
   
    all_scans = []
    for scan in scans:
        location = Location.objects(id=scan.location).first()
        robot = Robot.objects(id=scan.robot).first()

        scan_data = json.loads(scan.to_json())
        location_data = json.loads(location.to_json())
        robot_data = json.loads(robot.to_json())

        scan_data["location"] = location_data
        scan_data["robot"] = robot_data
        all_scans.append(scan_data)

    data = {
        "location": json.loads(location.to_json()),
        "scans": all_scans
    }

    return JSONResponse(content=data)

@router.get(
    "/scans/{id}"
)
async def get_scan(id: str):
    scan = Scan.objects(id=ObjectId(id)).first()

    if not scan:
        return JSONResponse(content={"error": "Scan not found"})

    location = Location.objects(id=scan.location).first()
    robot = Robot.objects(id=scan.robot).first()

    scan_data = json.loads(scan.to_json())
    location_data = json.loads(location.to_json())
    robot_data = json.loads(robot.to_json())

    scan_data["location"] = location_data
    scan_data["robot"] = robot_data

    return JSONResponse(content=scan_data)