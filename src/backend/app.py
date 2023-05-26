from fastapi import FastAPI
import uvicorn
import rclpy
from ros.setup import BackendController
import socketio
from eventlet import wsgi, listen
from routes import router
from dotenv import load_dotenv
import os
from mongoengine import *

load_dotenv()
uri = os.getenv("MONGODB_URI")

connect(host=uri)

#Cria um objeto API para o FASTAPI
app = FastAPI()
print(router)
app.include_router(router)

HOST = "127.0.0.1"  # localhost padrão
PORT = 3001  # Porta a ser utilizada

#iniciando o socket
sio = socketio.Server(async_handlers=True, logger=True,
                      ping_interval=120, ping_timeout=120)

websocket_app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('Connected to socket')

@sio.on('emergency_stop')
def stop(sid):
    sio.emit("emergency_stop")
    sio.sleep(0)
    
# Function to start the server
# def start_server():
    # wsgi.server(listen((HOST, PORT)), app)

def main():
    # start_server()
    uvicorn.run(app, host=HOST, port=PORT)

    rclpy.init()
    node = BackendController()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()