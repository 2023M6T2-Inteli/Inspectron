import fastapi
import uvicorn
import random
from fastapi.responses import RedirectResponse


#Cria um objeto API para o FASTAPI
api = fastapi.FastAPI()

import socketio
import socket
from eventlet import wsgi, listen


HOST = "127.0.0.1"  # localhost padrão
PORT = 65432  # Porta a ser utilizada

#iniciando o socket
sio = socketio.Server(async_handlers=True, logger=True,
                      ping_interval=120, ping_timeout=120)

app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('Connected to socket')

#recebendo o stream e mandando para o frontend
@sio.on('streaming')
def streaming(sid, data):
    sio.emit("streaming", data, skip_sid=True)

@sio.on('emergency_stop')
def stop(sid):
    sio.emit("emergency_stop")
    sio.sleep(0)
    
# Function to start the server
def start_server():

    wsgi.server(listen((HOST, PORT)), app)

    
def main():
    pass

if __name__ =="__main__":
    uvicorn.run(api)