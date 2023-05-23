import fastapi
from fastapi.responses import RedirectResponse
import uvicorn

import rclpy
from ros.setup import BackendController
import socketio
from eventlet import wsgi, listen

#Cria um objeto API para o FASTAPI
api = fastapi.FastAPI()

HOST = "127.0.0.1"  # localhost padrão
PORT = 65432  # Porta a ser utilizada

#iniciando o socket
sio = socketio.Server(async_handlers=True, logger=True,
                      ping_interval=120, ping_timeout=120)

app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
    print('Connected to socket')

@sio.on('emergency_stop')
def stop(sid):
    sio.emit("emergency_stop")
    sio.sleep(0)
    
# Function to start the server
def start_server():
    wsgi.server(listen((HOST, PORT)), app)

def main():
    start_server()
    uvicorn.run(api)

    rclpy.init()
    node = BackendController(sio)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =="__main__":
    main()