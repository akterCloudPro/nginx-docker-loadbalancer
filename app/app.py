from flask import Flask
import socket
container_id = socket.gethostname()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, from akterCloudPro - [CID]' + container_id 
