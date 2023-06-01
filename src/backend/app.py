from fastapi import FastAPI
import uvicorn
import rclpy
import socketio
from ros.setup import BackendController
from socketio import AsyncServer
from routes import location_router, robot_router, scan_router, user_router
from config import connect_to_database
import threading
from fastapi.middleware.cors import CORSMiddleware


#Cria um objeto API para o FASTAPI
app = FastAPI(debug=True)

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
                      ping_interval=120, ping_timeout=120, async_mode='asgi')

socketio_app = socketio.ASGIApp(sio, app)

@sio.event
def connect(sid, environ):
    print('Connected to socket')

@sio.on('emergency_stop')
def stop(sid):
    sio.emit("emergency_stop")
    sio.sleep(0)

def run_uvicorn():
    uvicorn.run(socketio_app, host=HOST, port=PORT)

def run_rclpy():
    rclpy.init()
    node = BackendController()
    rclpy.spin(node)
    rclpy.shutdown()
    
def main():
    connect_to_database()

    uvicorn_thread = threading.Thread(target=run_uvicorn)
    rclpy_thread = threading.Thread(target=run_rclpy)

    uvicorn_thread.start()
    rclpy_thread.start()

    uvicorn_thread.join()
    rclpy_thread.join()

if __name__ =="__main__":
    main()