from fastapi import APIRouter
from ..models.location import Location
from ..models.robot import Robot
from ..models.scan import Scan

router = APIRouter()

@router.get('/locations')
async def get_locations():
    locations = Location.objects()
    return locations.to_json()

@router.post('/locations/create')
async def create_location(body):
    location = Location(name=body['name'], coordinates=body['coordinates'])
    location.save()
    return location.to_json()

@router.get('/robot')
async def get_robots():
    robots = Robot.objects()
    return robots.to_json()

@router.post('/robot/create')
async def get_robots(body):
    robot = Robot(name=body['name'], ip=body['ip'])
    robot.save()
    return robot.to_json()

@router.get('/scan')
async def get_scans():
    scans = Scan.objects()
    return scans.to_json()