from fastapi import FastAPI, BackgroundTasks
import uvicorn
import rclpy
import socketio
from ros.setup import BackendController
from socketio import AsyncServer
from routes import location_router, robot_router, scan_router, user_router
from config import connect_to_database
import threading
from fastapi.middleware.cors import CORSMiddleware
from uvicorn.protocols.http.h11_impl import H11Protocol
import asyncio
import queue
from utils import NewScan
#Cria um objeto API para o FASTAPI
app = FastAPI(debug=True)

async def startup_event():
    while True:
        try:
            # Try to get an event from the queue
            event = event_queue.get_nowait()
        except queue.Empty:
            # If the queue is empty, sleep for a bit and then continue the loop
            await asyncio.sleep(0.1)
            continue
       
        # If we got an event, emit it
        await sio.emit(event['name'], event['data'])

# async def startup():
#     loop = asyncio.get_event_loop()
#     await loop.run_in_executor(None, startup_event)

@app.on_event("startup")
async def tste():
    # await startup()
    
    asyncio.create_task(startup_event())

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(location_router)
app.include_router(robot_router)
app.include_router(scan_router)
app.include_router(user_router)

HOST = "0.0.0.0"  # localhost padrão
PORT = 3001  # Porta a ser utilizada

#iniciando o socket
sio = AsyncServer(async_handlers=True, logger=True,
                      ping_interval=120, ping_timeout=120, async_mode='asgi', cors_allowed_origins='*')

event_queue = queue.Queue()

rclpy.init()
new_scan = NewScan()
node_backend = BackendController(sio=sio, event_queue=event_queue, new_scan=new_scan)

socketio_app = socketio.ASGIApp(sio, app)


@sio.event
async def connect(sid, environ):
    node_backend.heartbeat.send("oi")
    print('Connected to socket', flush=True)
    

@sio.on('emergency_stop')
def stop(sid):
    sio.emit("emergency_stop")
    sio.sleep(0)


@sio.on('new_scan_data')
def stop(sid, message):
    print(message, flush=True)

@sio.event
def disconnect(sid):
    print('Disconnected from socket')

# async def emit_events_from_queue():
#     while True:
#         print("oie", flush=True)
#         try:
#             # Try to get an event from the queue
#             event = event_queue.get_nowait()
#         except queue.Empty:
#             # If the queue is empty, sleep for a bit and then continue the loop
#             await asyncio.sleep(0.1)
#             continue
#         print(event, flush=True)
#         # If we got an event, emit it
#         await sio.emit(event['name'], event['data'])

def run_uvicorn():
    config = uvicorn.Config(
        socketio_app, 
        host=HOST, 
        port=PORT,
    )
    server = uvicorn.Server(config)
    
    server.run()

def run_rclpy():
    rclpy.spin(node_backend)
    rclpy.shutdown()
    
def main():
    connect_to_database()

    uvicorn_thread = threading.Thread(target=run_uvicorn)
    rclpy_thread = threading.Thread(target=run_rclpy)

    uvicorn_thread.start()
    rclpy_thread.start()

    uvicorn_thread.join()
    rclpy_thread.join()

if __name__ == "__main__":
    main()