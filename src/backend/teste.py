import socketio

# Create a SocketIO client instance
sio = socketio.Client()

# Define event handlers
@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.on('camera')
def my_event(data):
    print('Received event:', data)

# Connect to the SocketIO server
sio.connect('http://localhost:3001')

# Listen for events
sio.wait()